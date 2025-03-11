from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedbackContext")


@_attrs_define
class FeedbackContext:
    """Flexible dictionary to capture additional contextual information

    Example:
        {'user_role': 'researcher', 'interaction_length': 5, 'model_version': '3.5'}

    Attributes:
        user_role (Union[Unset, str]):
        interaction_length (Union[Unset, float]):
        model_version (Union[Unset, str]):
    """

    user_role: Union[Unset, str] = UNSET
    interaction_length: Union[Unset, float] = UNSET
    model_version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_role = self.user_role

        interaction_length = self.interaction_length

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_role is not UNSET:
            field_dict["user_role"] = user_role
        if interaction_length is not UNSET:
            field_dict["interaction_length"] = interaction_length
        if model_version is not UNSET:
            field_dict["model_version"] = model_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        user_role = d.pop("user_role", UNSET)

        interaction_length = d.pop("interaction_length", UNSET)

        model_version = d.pop("model_version", UNSET)

        feedback_context = cls(
            user_role=user_role,
            interaction_length=interaction_length,
            model_version=model_version,
        )

        feedback_context.additional_properties = d
        return feedback_context

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
