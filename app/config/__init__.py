# Standard library
import os
from logging.config import dictConfig

# Internal modules
from .logging import LOGGING_CONIFG
from .util import get_dsn

dictConfig(LOGGING_CONIFG)


SERVICE_NAME: str = "text-service"
SERVICE_VERSION: str = "1.0-RC"
SERVER_NAME: str = f"{SERVICE_NAME}/{SERVICE_VERSION}"
REQUEST_ID_HEADER: str = "X-Request-ID"
LANGUAGE_HEADER = "Accept-Language"
TEST_MODE: bool = os.getenv("TEST_MODE", "0") == "1"


class AppConfig:
    SQLALCHEMY_DATABASE_URI: str = get_dsn(TEST_MODE)
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

