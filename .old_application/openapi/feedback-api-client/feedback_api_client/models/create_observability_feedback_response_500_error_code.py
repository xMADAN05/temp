from enum import Enum


class CreateObservabilityFeedbackResponse500ErrorCode(str, Enum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"

    def __str__(self) -> str:
        return str(self.value)
