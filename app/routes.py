# Standard library
from typing import Any, Dict

# 3rd party modules.
import flask
from crazerace import http
from crazerace.http.security import secured

# Internal modules
from app import app
from app.config import JWT_SECRET
from app import controller


@app.route("/v1/texts/key/<key>", methods=["GET"])
@secured(JWT_SECRET)
def get_text(key: str) -> flask.Response:
    return controller.get_text_by_key(key)


@app.route("/v1/texts/group/<group_id>", methods=["GET"])
@secured(JWT_SECRET)
def get_text_group(group_id: str) -> flask.Response:
    return controller.get_text_group(group_id)


@app.route("/health", methods=["GET"])
def check_health() -> flask.Response:
    return controller.check_health()

