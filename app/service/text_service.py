# Standard library
from typing import Dict

# 3rd party modules
from crazerace.http.error import NotFoundError, BadRequestError
from crazerace.http.instrumentation import trace

# Internal modules
from app.models import TranslatedText, Language
from app.repository import text_repo, language_repo


@trace("text_service")
def get_text_by_key(key: str, language: str) -> Dict[str, str]:
    _assert_language_support(language)
    text = text_repo.find_by_key(key, language)
    if not text:
        raise NotFoundError()
    return {text.key: text.value}


@trace("text_service")
def _assert_language_support(language_id: str) -> Language:
    lang = language_repo.find_language(language_id)
    if not lang:
        raise BadRequestError(f"Unsupported language: {language_id}")
    return lang
