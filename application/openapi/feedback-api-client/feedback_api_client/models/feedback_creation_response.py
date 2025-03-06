import datetime
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.feedback_creation_response_status import FeedbackCreationResponseStatus

T = TypeVar("T", bound="FeedbackCreationResponse")


@_attrs_define
class FeedbackCreationResponse:
    """Response for successful feedback creation

    Attributes:
        status (FeedbackCreationResponseStatus): Indicates successful creation of feedback
        feedback_id (UUID): Unique identifier for the created feedback record Example:
            1309860b-eb8d-4da6-b279-68a4d7c49f7b.
        timestamp (datetime.datetime): Timestamp of feedback creation Example: 2024-03-05T12:34:56.789Z.
    """

    status: FeedbackCreationResponseStatus
    feedback_id: UUID
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        feedback_id = str(self.feedback_id)

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "feedback_id": feedback_id,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status = FeedbackCreationResponseStatus(d.pop("status"))

        feedback_id = UUID(d.pop("feedback_id"))

        timestamp = isoparse(d.pop("timestamp"))

        feedback_creation_response = cls(
            status=status,
            feedback_id=feedback_id,
            timestamp=timestamp,
        )

        feedback_creation_response.additional_properties = d
        return feedback_creation_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
