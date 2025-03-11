from enum import Enum


class GetObservabilityFeedbackResponse404ErrorCode(str, Enum):
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
