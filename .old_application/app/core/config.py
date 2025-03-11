"""Module that defines the applications config"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Encapsulates application configuration parameters.
           
    This class defines all configurable parameters for the application,
    with sensible defaults that can be overridden via environment variables
    or an .env file.
    """

    project_name: str = "Feedback Service"
    """The name of the project. """

    log_level: str = "INFO"
    """The logging level for the application."""

    api_v1_prefix: str = "/v1/feedback"
    """The prefix for the API version 1 endpoints."""

    FEEDBACK_API_URL: str = "http://localhost:8005"
    """The URL for the feedback API."""

    # OPENAPI_FILEPATH: str = './docs/openapi.yaml'

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    """Pydantic settings configurations"""

# create singleton instance for global use
settings = Settings()