from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_observability_feedback_response_400_error_code import (
    CreateObservabilityFeedbackResponse400ErrorCode,
)

T = TypeVar("T", bound="CreateObservabilityFeedbackResponse400Error")


@_attrs_define
class CreateObservabilityFeedbackResponse400Error:
    """
    Attributes:
        code (CreateObservabilityFeedbackResponse400ErrorCode):
        message (str): Detailed error message
    """

    code: CreateObservabilityFeedbackResponse400ErrorCode
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        code = CreateObservabilityFeedbackResponse400ErrorCode(d.pop("code"))

        message = d.pop("message")

        create_observability_feedback_response_400_error = cls(
            code=code,
            message=message,
        )

        create_observability_feedback_response_400_error.additional_properties = d
        return create_observability_feedback_response_400_error

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
