from enum import Enum


class CreateObservabilityFeedbackResponse400ErrorCode(str, Enum):
    BAD_REQUEST = "BAD_REQUEST"

    def __str__(self) -> str:
        return str(self.value)
