"""Commits an image into the project's public assets/ folder and pushes it,
so it has a raw.githubusercontent.com URL that Instagram's API can fetch.

See decision 0003 for why this approach is used instead of a hosting service.
"""

import os
import re
import subprocess

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
ASSETS_DIR = os.path.join(REPO_ROOT, "assets")


def _run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def _parse_owner_repo(remote_url: str) -> tuple[str, str]:
    match = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", remote_url)
    if not match:
        raise RuntimeError(f"Could not parse GitHub owner/repo from remote URL: {remote_url}")
    return match.group(1), match.group(2)


def publish_image_and_get_url(image_path: str) -> str:
    filename = os.path.basename(image_path)
    dest_path = os.path.join(ASSETS_DIR, filename)

    os.makedirs(ASSETS_DIR, exist_ok=True)
    with open(image_path, "rb") as src, open(dest_path, "wb") as dst:
        dst.write(src.read())

    relative_path = f"assets/{filename}"
    _run_git("add", relative_path)

    status = _run_git("status", "--porcelain", relative_path)
    if status:
        _run_git("commit", "-m", f"Add {relative_path} for Instagram post")
        _run_git("push")

    remote_url = _run_git("remote", "get-url", "origin")
    owner, repo = _parse_owner_repo(remote_url)
    branch = _run_git("rev-parse", "--abbrev-ref", "HEAD")

    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{relative_path}"
