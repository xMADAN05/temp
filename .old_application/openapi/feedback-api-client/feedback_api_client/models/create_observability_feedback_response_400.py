from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_observability_feedback_response_400_error import CreateObservabilityFeedbackResponse400Error


T = TypeVar("T", bound="CreateObservabilityFeedbackResponse400")


@_attrs_define
class CreateObservabilityFeedbackResponse400:
    """
    Attributes:
        error (CreateObservabilityFeedbackResponse400Error):
    """

    error: "CreateObservabilityFeedbackResponse400Error"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_observability_feedback_response_400_error import (
            CreateObservabilityFeedbackResponse400Error,
        )

        d = src_dict.copy()
        error = CreateObservabilityFeedbackResponse400Error.from_dict(d.pop("error"))

        create_observability_feedback_response_400 = cls(
            error=error,
        )

        create_observability_feedback_response_400.additional_properties = d
        return create_observability_feedback_response_400

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
