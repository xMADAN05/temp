from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delete_observability_feedback_response_404_error import DeleteObservabilityFeedbackResponse404Error


T = TypeVar("T", bound="DeleteObservabilityFeedbackResponse404")


@_attrs_define
class DeleteObservabilityFeedbackResponse404:
    """
    Attributes:
        error (DeleteObservabilityFeedbackResponse404Error):
    """

    error: "DeleteObservabilityFeedbackResponse404Error"
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
        from ..models.delete_observability_feedback_response_404_error import (
            DeleteObservabilityFeedbackResponse404Error,
        )

        d = src_dict.copy()
        error = DeleteObservabilityFeedbackResponse404Error.from_dict(d.pop("error"))

        delete_observability_feedback_response_404 = cls(
            error=error,
        )

        delete_observability_feedback_response_404.additional_properties = d
        return delete_observability_feedback_response_404

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
