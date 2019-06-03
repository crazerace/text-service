# Standard libraries
from typing import List, Optional

# 3rd party libraries
from crazerace.http.instrumentation import trace

# Internal modules
from app.models import Language, TranslatedText, Group


@trace("text_repo")
def find_by_key(key: str, language: str) -> Optional[TranslatedText]:
    return TranslatedText.query.filter(
        TranslatedText.key == key, TranslatedText.language == language
    ).first()

