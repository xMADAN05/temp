from datetime import datetime
from pydantic import BaseModel
from typing import Dict, Any, Optional

class FeedbackServiceRequest(BaseModel):
    inference_id: str
    racfid: str
    application_id: Optional[str]
    timestamp: int = int(datetime.now().timestamp())
    feedback_relevance: Optional[str]
    feedback_type: Optional[str]
    guardrail_failure_type: Optional[str]
    context: Dict[str, Any] = {}

class FeedbackServiceResponse(BaseModel):
    id: str
    status: str

class ErrorResponse(BaseModel):
    detail: Any
    status_code: int