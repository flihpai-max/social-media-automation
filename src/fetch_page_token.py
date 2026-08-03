"""One-time helper: exchanges the Business Manager System User token in .env
for the Page-scoped access token needed to post, and rewrites .env in place.

Usage:
    python src/fetch_page_token.py
"""

import os
import re
import sys

import requests
from dotenv import load_dotenv

GRAPH_API_VERSION = "v19.0"
ENV_PATH = os.path.join(os.path.dirname(__file__), "..", ".env")


def main() -> int:
    load_dotenv(ENV_PATH)
    page_id = os.environ.get("FB_PAGE_ID")
    system_user_token = os.environ.get("FB_PAGE_ACCESS_TOKEN")

    if not page_id or not system_user_token:
        print("ERROR: FB_PAGE_ID and FB_PAGE_ACCESS_TOKEN must both be set in .env.", file=sys.stderr)
        return 1

    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}"
    response = requests.get(
        url,
        params={"fields": "access_token", "access_token": system_user_token},
        timeout=30,
    )
    body = response.json()

    if response.status_code != 200 or "access_token" not in body:
        error = body.get("error", {})
        print(f"ERROR: could not fetch Page token (HTTP {response.status_code}): {error.get('message', body)}", file=sys.stderr)
        return 1

    page_token = body["access_token"]

    with open(ENV_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"^FB_PAGE_ACCESS_TOKEN=.*$",
        f"FB_PAGE_ACCESS_TOKEN={page_token}",
        content,
        flags=re.MULTILINE,
    )

    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("SUCCESS: .env updated with the Page-scoped access token.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
