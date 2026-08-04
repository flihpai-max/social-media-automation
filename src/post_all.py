"""Posts a single image with a caption to Facebook, Instagram, and LinkedIn in one run.

Usage:
    python src/post_all.py path/to/image.jpg "Caption text"

Each platform is attempted independently — a failure on one platform doesn't
block the others (rule 8: errors are visible, not swallowed). Exits non-zero
if any platform failed, so a scheduled run (e.g. GitHub Actions) shows up as
a failed run when something needs attention.
"""

import os
import sys

from dotenv import load_dotenv

import facebook_post
import instagram_post
import linkedin_post


def run_facebook(image_path: str, caption: str) -> tuple[bool, str]:
    page_id = os.environ.get("FB_PAGE_ID")
    access_token = os.environ.get("FB_PAGE_ACCESS_TOKEN")
    if not page_id or not access_token:
        return False, "FB_PAGE_ID and FB_PAGE_ACCESS_TOKEN must both be set."

    try:
        result = facebook_post.post_image_to_page(page_id, access_token, image_path, caption)
        return True, f"post id {result.get('post_id', result.get('id'))}"
    except Exception as exc:
        return False, str(exc)


def run_instagram(image_path: str, caption: str) -> tuple[bool, str]:
    page_id = os.environ.get("FB_PAGE_ID")
    access_token = os.environ.get("FB_PAGE_ACCESS_TOKEN")
    if not page_id or not access_token:
        return False, "FB_PAGE_ID and FB_PAGE_ACCESS_TOKEN must both be set."

    try:
        ig_user_id = instagram_post.get_instagram_business_account_id(page_id, access_token)
        image_url = instagram_post.publish_image_and_get_url(image_path)
        creation_id = instagram_post.create_media_container(ig_user_id, access_token, image_url, caption)
        instagram_post.wait_until_ready(creation_id, access_token)
        result = instagram_post.publish_media(ig_user_id, access_token, creation_id)
        return True, f"post id {result['id']}"
    except Exception as exc:
        return False, str(exc)


def run_linkedin(image_path: str, caption: str) -> tuple[bool, str]:
    access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    if not access_token:
        return False, "LINKEDIN_ACCESS_TOKEN must be set (run src/linkedin_auth.py)."

    try:
        person_urn = linkedin_post.get_person_urn(access_token)
        upload_url, image_urn = linkedin_post.initialize_image_upload(access_token, person_urn)
        linkedin_post.upload_image_bytes(upload_url, access_token, image_path)
        post_id = linkedin_post.create_post(access_token, person_urn, image_urn, caption)
        return True, f"post id {post_id}"
    except Exception as exc:
        return False, str(exc)


PLATFORMS = [
    ("Facebook", run_facebook),
    ("Instagram", run_instagram),
    ("LinkedIn", run_linkedin),
]


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python src/post_all.py <image_path> <caption>", file=sys.stderr)
        return 1

    image_path, caption = sys.argv[1], sys.argv[2]

    load_dotenv()

    if not os.path.isfile(image_path):
        print(f"ERROR: image file not found: {image_path}", file=sys.stderr)
        return 1

    results = []
    for name, runner in PLATFORMS:
        success, detail = runner(image_path, caption)
        results.append((name, success, detail))
        status = "SUCCESS" if success else "FAILED"
        print(f"[{status}] {name}: {detail}")

    failures = [name for name, success, _ in results if not success]
    if failures:
        print(f"ERROR: {len(failures)} of {len(results)} platform(s) failed: {', '.join(failures)}", file=sys.stderr)
        return 1

    print(f"SUCCESS: posted to all {len(results)} platforms.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
