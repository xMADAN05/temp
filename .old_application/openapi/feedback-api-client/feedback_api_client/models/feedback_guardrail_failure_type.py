from enum import Enum


class FeedbackGuardrailFailureType(str, Enum):
    BIAS = "bias"
    HALLUCINATION = "hallucination"
    INAPPROPRIATE_CONTENT = "inappropriate_content"
    PROFANITY = "profanity"

    def __str__(self) -> str:
        return str(self.value)
