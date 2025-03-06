from enum import Enum


class FeedbackFeedbackType(str, Enum):
    GUARDRAIL_FAILURE = "guardrail_failure"
    PERFORMANCE_ISSUE = "performance_issue"
    USABILITY = "usability"

    def __str__(self) -> str:
        return str(self.value)
