"""One-time OAuth setup for LinkedIn: opens your browser to approve the app,
catches the redirect locally, exchanges the code for an access token, and
writes LINKEDIN_ACCESS_TOKEN into .env.

Usage:
    python src/linkedin_auth.py

Requires LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET to already be set in
.env, and http://localhost:8765/callback to be added as an authorized
redirect URL on the LinkedIn Developer App (Auth tab).
"""

import http.server
import os
import re
import secrets
import sys
import threading
import urllib.parse
import webbrowser

import requests
from dotenv import load_dotenv

REDIRECT_URI = "http://localhost:8765/callback"
SCOPES = "openid profile w_member_social"
ENV_PATH = os.path.join(os.path.dirname(__file__), "..", ".env")

_auth_code: str | None = None
_expected_state: str = secrets.token_urlsafe(16)


class _CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        global _auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        if params.get("state", [None])[0] != _expected_state:
            self.wfile.write(b"State mismatch. You can close this tab.")
            return

        if "code" in params:
            _auth_code = params["code"][0]
            self.wfile.write(b"Authorized. You can close this tab and return to the terminal.")
        else:
            self.wfile.write(f"Authorization failed: {params.get('error_description', ['unknown error'])[0]}".encode())

    def log_message(self, format: str, *args) -> None:
        pass


def wait_for_auth_code() -> str:
    server = http.server.HTTPServer(("localhost", 8765), _CallbackHandler)
    thread = threading.Thread(target=server.handle_request)
    thread.start()
    thread.join(timeout=180)
    server.server_close()

    if _auth_code is None:
        raise RuntimeError("Timed out waiting for LinkedIn authorization. Try again.")

    return _auth_code


def exchange_code_for_token(code: str, client_id: str, client_secret: str) -> str:
    response = requests.post(
        "https://www.linkedin.com/oauth/v2/accessToken",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": client_id,
            "client_secret": client_secret,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )
    body = response.json()

    if response.status_code != 200 or "access_token" not in body:
        raise RuntimeError(f"Token exchange failed (HTTP {response.status_code}): {body}")

    return body["access_token"]


def write_token_to_env(token: str) -> None:
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"^LINKEDIN_ACCESS_TOKEN=.*$",
        f"LINKEDIN_ACCESS_TOKEN={token}",
        content,
        flags=re.MULTILINE,
    )

    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main() -> int:
    load_dotenv(ENV_PATH)
    client_id = os.environ.get("LINKEDIN_CLIENT_ID")
    client_secret = os.environ.get("LINKEDIN_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("ERROR: LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET must both be set in .env.", file=sys.stderr)
        return 1

    auth_url = "https://www.linkedin.com/oauth/v2/authorization?" + urllib.parse.urlencode(
        {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": REDIRECT_URI,
            "scope": SCOPES,
            "state": _expected_state,
        }
    )

    print("Opening your browser to approve the app. Log in and click Allow if prompted.")
    webbrowser.open(auth_url)

    try:
        code = wait_for_auth_code()
        token = exchange_code_for_token(code, client_id, client_secret)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    write_token_to_env(token)
    print("SUCCESS: .env updated with LINKEDIN_ACCESS_TOKEN.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
