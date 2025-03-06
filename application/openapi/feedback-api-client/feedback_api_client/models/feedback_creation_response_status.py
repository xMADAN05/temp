from enum import Enum


class FeedbackCreationResponseStatus(str, Enum):
    CREATED = "Created"

    def __str__(self) -> str:
        return str(self.value)
