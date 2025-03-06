"""
Module for application logging configuration.

This module provides structured JSON logging with request context tracking
and configurable output formatting.
"""

import json
import logging
from contextvars import ContextVar

from fastapi import Request

from app.core.config import settings

request_id: ContextVar[Request | None] = ContextVar("request_id", default=None)


class CustomJsonFormatter(logging.Formatter):
    """Custom log formatter for JSON outputs"""

    excluded_fields = [
        "msg",
        "args",
        "levelno",
        "pathname",
        "filename",
        "lineno",
        "funcName",
        "msecs",
        "relativeCreated",
        "thread",
        "threadName",
        "processName",
        "process",
        "created",
        "module",
    ]

    def format(self, record: logging.LogRecord) -> str:
        """Formats a log entry as JSON"""

        # Set Timestamp in required format
        record.timestamp = super().formatTime(record, datefmt="%d-%m-%Y %H:%M:%S %z")

        super().format(record)

        output = {
            k: str(v)
            for k, v in record.__dict__.items()
            if k not in self.excluded_fields and v
        }
        return json.dumps(output)


class ContextFilter(logging.Filter):
    """Custom log filter for JSON outputs"""

    def filter(self, record):
        request = request_id.get()

        if request:
            record.id = request.state.id
            record.method = request.method
            record.path = request.url.path

        return True


logging_config = {
    "version": 1,
    # Leave any existing loggers to continue working
    "disable_existing_loggers": False,
    # Filters go here
    "filters": {
        "contextFilter": {
            "()": "app.core.logging.ContextFilter",
        }
    },
    # All handlers go here
    "handlers": {
        # Create a basic console handler
        "console": {
            # Define class of handler
            "class": "logging.StreamHandler",
            # Add formatter to handler
            "formatter": "customJson",
            "filters": ["contextFilter"],
        },
    },
    "root": {
        "handlers": ["console"],
        "level": settings.LOG_LEVEL,
    },
    # Define custom loggers that you will reference within the project through logging.getLogger
    "loggers": {},
    "formatters": {"customJson": {"()": "app.core.logging.CustomJsonFormatter"}},
}
