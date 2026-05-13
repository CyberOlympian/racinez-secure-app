from __future__ import annotations

import os
import re
from typing import Final

from flask import Flask, jsonify, request

APP_NAME: Final[str] = "secure-app"
NAME_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Za-z][A-Za-z0-9 _-]{0,31}$")
DEFAULT_PORT: Final[int] = 8000


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.update(
        TESTING=False,
        JSON_SORT_KEYS=False,
        MAX_CONTENT_LENGTH=1024,
    )

    @app.after_request
    def add_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.get("/health")
    def health():
        return jsonify(service=APP_NAME, status="ok")

    @app.get("/greet")
    def greet():
        raw_name = request.args.get("name", "world")
        name = raw_name.strip()

    if len(name) < 2:
    return jsonify(error="name too short"), 400

        return jsonify(message=f"Hello, {name}!")

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", DEFAULT_PORT))
    app.run(host="0.0.0.0", port=port)
