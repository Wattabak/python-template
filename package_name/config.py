from logging.config import dictConfig
from typing import Any

from pydantic import BaseSettings

__all__ = [
    'settings'
]


class AppSettings(BaseSettings):
    DATABASE_URL: str
    LOGGING_CONFIG: dict[str, Any] = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',  # Default is stderr
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': False
            },
            '__main__': {  # if __name__ == '__main__'
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': False
            },
        }
    }


settings = AppSettings()

dictConfig(settings.LOGGING_CONFIG)
