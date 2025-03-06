from enum import Enum


class DeleteObservabilityFeedbackResponse404ErrorCode(str, Enum):
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
