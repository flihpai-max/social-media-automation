"""Posts a single image with a caption to an Instagram Business account via the Graph API.

Usage:
    python src/instagram_post.py path/to/image.jpg "Caption text"

Required environment variables (see .env.example):
    FB_PAGE_ID
    FB_PAGE_ACCESS_TOKEN

The Instagram Business account must be linked to the Facebook Page identified
by FB_PAGE_ID. The image is committed to the repo's assets/ folder and pushed
so Instagram can fetch it over a public URL (see decision 0003).
"""

import os
import sys
import time

import requests
from dotenv import load_dotenv

from github_image_host import publish_image_and_get_url

GRAPH_API_VERSION = "v19.0"
POLL_ATTEMPTS = 10
POLL_DELAY_SECONDS = 3


def get_instagram_business_account_id(page_id: str, access_token: str) -> str:
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}"
    response = requests.get(
        url,
        params={"fields": "instagram_business_account", "access_token": access_token},
        timeout=30,
    )
    body = response.json()

    if response.status_code != 200 or "instagram_business_account" not in body:
        error = body.get("error", {})
        raise RuntimeError(
            f"Could not find an Instagram Business account linked to Page {page_id} "
            f"(HTTP {response.status_code}): {error.get('message', body)}"
        )

    return body["instagram_business_account"]["id"]


def create_media_container(ig_user_id: str, access_token: str, image_url: str, caption: str) -> str:
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{ig_user_id}/media"
    response = requests.post(
        url,
        data={"image_url": image_url, "caption": caption, "access_token": access_token},
        timeout=30,
    )
    body = response.json()

    if response.status_code != 200 or "id" not in body:
        error = body.get("error", {})
        raise RuntimeError(f"Failed to create Instagram media container (HTTP {response.status_code}): {error.get('message', body)}")

    return body["id"]


def wait_until_ready(creation_id: str, access_token: str) -> None:
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{creation_id}"
    for _ in range(POLL_ATTEMPTS):
        response = requests.get(url, params={"fields": "status_code", "access_token": access_token}, timeout=30)
        body = response.json()
        status_code = body.get("status_code")

        if status_code == "FINISHED":
            return
        if status_code == "ERROR":
            raise RuntimeError(f"Instagram failed to process the media container: {body}")

        time.sleep(POLL_DELAY_SECONDS)

    raise RuntimeError("Timed out waiting for Instagram to finish processing the media container.")


def publish_media(ig_user_id: str, access_token: str, creation_id: str) -> dict:
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{ig_user_id}/media_publish"
    response = requests.post(
        url,
        data={"creation_id": creation_id, "access_token": access_token},
        timeout=30,
    )
    body = response.json()

    if response.status_code != 200 or "id" not in body:
        error = body.get("error", {})
        raise RuntimeError(f"Failed to publish Instagram post (HTTP {response.status_code}): {error.get('message', body)}")

    return body


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python src/instagram_post.py <image_path> <caption>", file=sys.stderr)
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
        ig_user_id = get_instagram_business_account_id(page_id, access_token)
        image_url = publish_image_and_get_url(image_path)
        creation_id = create_media_container(ig_user_id, access_token, image_url, caption)
        wait_until_ready(creation_id, access_token)
        result = publish_media(ig_user_id, access_token, creation_id)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"SUCCESS: posted to Instagram Business account {ig_user_id} — post id {result['id']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
