from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_observability_feedback_response_500_error import GetObservabilityFeedbackResponse500Error


T = TypeVar("T", bound="GetObservabilityFeedbackResponse500")


@_attrs_define
class GetObservabilityFeedbackResponse500:
    """
    Attributes:
        error (GetObservabilityFeedbackResponse500Error):
    """

    error: "GetObservabilityFeedbackResponse500Error"
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
        from ..models.get_observability_feedback_response_500_error import GetObservabilityFeedbackResponse500Error

        d = src_dict.copy()
        error = GetObservabilityFeedbackResponse500Error.from_dict(d.pop("error"))

        get_observability_feedback_response_500 = cls(
            error=error,
        )

        get_observability_feedback_response_500.additional_properties = d
        return get_observability_feedback_response_500

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
