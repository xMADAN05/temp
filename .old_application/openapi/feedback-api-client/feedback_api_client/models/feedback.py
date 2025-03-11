from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feedback_feedback_relevance import FeedbackFeedbackRelevance
from ..models.feedback_feedback_type import FeedbackFeedbackType
from ..models.feedback_guardrail_failure_type import FeedbackGuardrailFailureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feedback_context import FeedbackContext


T = TypeVar("T", bound="Feedback")


@_attrs_define
class Feedback:
    """Schema for submitting feedback

    Attributes:
        application_id (UUID): The ID of the application the document analysis request was for Example:
            1309860b-eb8d-4da6-b279-68a4d7c49f7b.
        inference_id (str): Unique identifier for the specific AI inference Example: inf_123456789abcdef.
        racfid (str): User identifier (RACF ID) submitting the feedback Example: A123456.
        timestamp (Union[Unset, int]): Unix timestamp of when the feedback was submitted
        feedback_relevance (Union[Unset, FeedbackFeedbackRelevance]): Binary indicator of feedback relevance Example: 1.
        feedback_type (Union[Unset, FeedbackFeedbackType]): Categorization of feedback type Example: guardrail_failure.
        guardrail_failure_type (Union[Unset, FeedbackGuardrailFailureType]): The type of guardrail violation Example:
            hallucination.
        context (Union[Unset, FeedbackContext]): Flexible dictionary to capture additional contextual information
            Example: {'user_role': 'researcher', 'interaction_length': 5, 'model_version': '3.5'}.
    """

    application_id: UUID
    inference_id: str
    racfid: str
    timestamp: Union[Unset, int] = UNSET
    feedback_relevance: Union[Unset, FeedbackFeedbackRelevance] = UNSET
    feedback_type: Union[Unset, FeedbackFeedbackType] = UNSET
    guardrail_failure_type: Union[Unset, FeedbackGuardrailFailureType] = UNSET
    context: Union[Unset, "FeedbackContext"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = str(self.application_id)

        inference_id = self.inference_id

        racfid = self.racfid

        timestamp = self.timestamp

        feedback_relevance: Union[Unset, str] = UNSET
        if not isinstance(self.feedback_relevance, Unset):
            feedback_relevance = self.feedback_relevance.value

        feedback_type: Union[Unset, str] = UNSET
        if not isinstance(self.feedback_type, Unset):
            feedback_type = self.feedback_type.value

        guardrail_failure_type: Union[Unset, str] = UNSET
        if not isinstance(self.guardrail_failure_type, Unset):
            guardrail_failure_type = self.guardrail_failure_type.value

        context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "application_id": application_id,
                "inference_id": inference_id,
                "racfid": racfid,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if feedback_relevance is not UNSET:
            field_dict["feedback_relevance"] = feedback_relevance
        if feedback_type is not UNSET:
            field_dict["feedback_type"] = feedback_type
        if guardrail_failure_type is not UNSET:
            field_dict["guardrail_failure_type"] = guardrail_failure_type
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.feedback_context import FeedbackContext

        d = src_dict.copy()
        application_id = UUID(d.pop("application_id"))

        inference_id = d.pop("inference_id")

        racfid = d.pop("racfid")

        timestamp = d.pop("timestamp", UNSET)

        _feedback_relevance = d.pop("feedback_relevance", UNSET)
        feedback_relevance: Union[Unset, FeedbackFeedbackRelevance]
        if isinstance(_feedback_relevance, Unset):
            feedback_relevance = UNSET
        else:
            feedback_relevance = FeedbackFeedbackRelevance(_feedback_relevance)

        _feedback_type = d.pop("feedback_type", UNSET)
        feedback_type: Union[Unset, FeedbackFeedbackType]
        if isinstance(_feedback_type, Unset):
            feedback_type = UNSET
        else:
            feedback_type = FeedbackFeedbackType(_feedback_type)

        _guardrail_failure_type = d.pop("guardrail_failure_type", UNSET)
        guardrail_failure_type: Union[Unset, FeedbackGuardrailFailureType]
        if isinstance(_guardrail_failure_type, Unset):
            guardrail_failure_type = UNSET
        else:
            guardrail_failure_type = FeedbackGuardrailFailureType(_guardrail_failure_type)

        _context = d.pop("context", UNSET)
        context: Union[Unset, FeedbackContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = FeedbackContext.from_dict(_context)

        feedback = cls(
            application_id=application_id,
            inference_id=inference_id,
            racfid=racfid,
            timestamp=timestamp,
            feedback_relevance=feedback_relevance,
            feedback_type=feedback_type,
            guardrail_failure_type=guardrail_failure_type,
            context=context,
        )

        feedback.additional_properties = d
        return feedback

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
