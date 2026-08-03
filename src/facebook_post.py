"""Posts a single image with a caption to a Facebook Page via the Graph API.

Usage:
    python src/facebook_post.py path/to/image.jpg "Caption text"

Required environment variables (see .env.example):
    FB_PAGE_ID
    FB_PAGE_ACCESS_TOKEN
"""

import os
import sys

import requests
from dotenv import load_dotenv

GRAPH_API_VERSION = "v19.0"


def post_image_to_page(page_id: str, access_token: str, image_path: str, caption: str) -> dict:
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}/photos"

    with open(image_path, "rb") as image_file:
        response = requests.post(
            url,
            data={"message": caption, "access_token": access_token},
            files={"source": image_file},
            timeout=30,
        )

    body = response.json()

    if response.status_code != 200 or "error" in body:
        error = body.get("error", {})
        raise RuntimeError(
            f"Facebook post failed (HTTP {response.status_code}): "
            f"{error.get('message', body)}"
        )

    return body


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python src/facebook_post.py <image_path> <caption>", file=sys.stderr)
        return 1

    image_path, caption = sys.argv[1], sys.argv[2]

    load_dotenv()
    page_id = os.environ.get("FB_PAGE_ID")
    access_token = os.environ.get("FB_PAGE_ACCESS_TOKEN")

    if not page_id or not access_token:
        print(
            "ERROR: FB_PAGE_ID and FB_PAGE_ACCESS_TOKEN must both be set "
            "(as environment variables or in a local .env file).",
            file=sys.stderr,
        )
        return 1

    if not os.path.isfile(image_path):
        print(f"ERROR: image file not found: {image_path}", file=sys.stderr)
        return 1

    try:
        result = post_image_to_page(page_id, access_token, image_path, caption)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"SUCCESS: posted to Facebook Page {page_id} — post id {result.get('post_id', result.get('id'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
