# Standard library
import logging

# 3rd party modules
import flask
from flask import jsonify, make_response, request
from crazerace import http
from crazerace.http import status
from crazerace.http.error import BadRequestError
from crazerace.http.instrumentation import trace

# Internal modules
from app.config import LANGUAGE_HEADER
from app.service import health
from app.service import text_service


_log = logging.getLogger(__name__)


@trace("controller")
def get_text_by_key(key: str) -> flask.Response:
    text = text_service.get_text_by_key(key, _get_language())
    return http.create_response(text)


@trace("controller")
def get_text_group(group_id: str) -> flask.Response:
    texts = text_service.get_text_by_group(group_id, _get_language())
    return http.create_response(texts)


@trace("controller")
def check_health() -> flask.Response:
    health_status = health.check()
    return http.create_response(health_status)


def _get_language() -> str:
    lang = request.headers.get(LANGUAGE_HEADER)
    if not lang:
        raise BadRequestError("No language specified")
    return lang
