from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import List, Optional
from uuid import UUID

from app.services.dynamodb_dao import FeedbackService
from app.models.feedback_models import FeedbackServiceRequest, FeedbackServiceResponse

from app.core.auth import BearerAuth, security


feedback_service = FeedbackService()

async def submit_feedback(feedback: FeedbackServiceRequest,
                    authenticated: bool = Depends(security)) -> FeedbackServiceResponse:
    if not authenticated:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    try:
        response = await feedback_service.submit_feedback(feedback=feedback)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Failed to submit feedback: {str(e)}")

async def get_feedback_by_id(feedback_id: str,
                            authenticated: bool = Depends(security))-> FeedbackServiceRequest:
    if not authenticated:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    try:
        response = await feedback_service.get_feedback(feedback_id=feedback_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Failed to retrieve feedback: {str(e)}")

async def get_feedback_by_racfid(racfid: str,
                            authenticated: bool = Depends(security))-> List[FeedbackServiceRequest]:
    if not authenticated:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    try:
        response = await feedback_service.get_feedback_by_rafcid(racfid=racfid)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Failed to retrieve feedback by RACFID: {str(e)}")

async def get_feedback_by_application_id(application_id: str,
                            authenticated: bool = Depends(security))-> List[FeedbackServiceRequest]:
    if not authenticated:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    try:
        response = await feedback_service.get_feedback_by_application_id(application_id=application_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Failed to retrieve feedback by Application ID: {str(e)}")

async def delete_feedback_by_feedback_id(feedback_id: str,
                    authenticated: bool = Depends(security))-> FeedbackServiceResponse:
    if not authenticated:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    try:
        response = await feedback_service.delete_feedback_by_id(feedback_id=feedback_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Failed to delete feedback by Feedback ID: {str(e)}")


async def delete_feedback_by_application_id(application_id: str,
                    authenticated: bool = Depends(security))-> FeedbackServiceResponse:
    pass
