"""One-time local admin tool: sets this repo's GitHub Actions secrets via the
API instead of the web UI's paste field, to avoid manual copy/paste corruption.

Usage:
    python tools/set_github_secrets.py

Requires GITHUB_PAT in .env — a fine-grained GitHub Personal Access Token
scoped to this repo with "Secrets: Read and write" permission. Reads the
values to upload directly from .env (FB_PAGE_ID, FB_PAGE_ACCESS_TOKEN,
LINKEDIN_ACCESS_TOKEN) — never printed to the console.
"""

import base64
import os
import re
import subprocess
import sys

import requests
from dotenv import load_dotenv
from nacl import encoding, public

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
ENV_PATH = os.path.join(REPO_ROOT, ".env")
SECRET_NAMES = ["FB_PAGE_ID", "FB_PAGE_ACCESS_TOKEN", "LINKEDIN_ACCESS_TOKEN"]


def get_owner_repo() -> tuple[str, str]:
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    match = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", result.stdout.strip())
    if not match:
        raise RuntimeError(f"Could not parse GitHub owner/repo from remote URL: {result.stdout}")
    return match.group(1), match.group(2)


def encrypt_secret(public_key_b64: str, secret_value: str) -> str:
    public_key = public.PublicKey(public_key_b64.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return base64.b64encode(encrypted).decode("utf-8")


def main() -> int:
    load_dotenv(ENV_PATH)
    pat = os.environ.get("GITHUB_PAT")

    if not pat:
        print("ERROR: GITHUB_PAT must be set in .env.", file=sys.stderr)
        return 1

    missing = [name for name in SECRET_NAMES if not os.environ.get(name)]
    if missing:
        print(f"ERROR: the following must be set in .env before uploading: {', '.join(missing)}", file=sys.stderr)
        return 1

    owner, repo = get_owner_repo()
    headers = {
        "Authorization": f"Bearer {pat}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    key_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/actions/secrets/public-key",
        headers=headers,
        timeout=30,
    )
    if key_response.status_code != 200:
        print(f"ERROR: could not fetch repo public key (HTTP {key_response.status_code}): {key_response.json()}", file=sys.stderr)
        return 1

    key_data = key_response.json()

    for name in SECRET_NAMES:
        value = os.environ[name]
        encrypted_value = encrypt_secret(key_data["key"], value)

        response = requests.put(
            f"https://api.github.com/repos/{owner}/{repo}/actions/secrets/{name}",
            headers=headers,
            json={"encrypted_value": encrypted_value, "key_id": key_data["key_id"]},
            timeout=30,
        )

        if response.status_code not in (201, 204):
            print(f"[FAILED] {name}: HTTP {response.status_code}: {response.text}", file=sys.stderr)
        else:
            print(f"[SUCCESS] {name}: secret set (HTTP {response.status_code})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
