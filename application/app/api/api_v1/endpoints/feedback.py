"""
AI Feedback Service Routes

This module defines the FastAPI routes for the AI Feedback Service.
It provides endpoints for submitting, retrieving, and deleting feedback
related to AI services, with appropriate authentication and validation.
"""

import logging
from datetime import datetime
from uuid import uuid4
from http import HTTPStatus
from typing import Annotated, Any, List, Optional, Dict
from fastapi import APIRouter, Body, Header, Response, Request, HTTPException, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from app.services.dynamodb_dao import FeedbackService
from app.models.feedback_models import FeedbackServiceRequest, FeedbackServiceResponse, ErrorResponse
from app.services.dynamodb_services import (
    get_feedback,
    submit_feedback,
    get_feedback_by_id,
    delete_feedback_by_feedback_id,
    delete_feedback_by_application_id
) 

logger = logging.getLogger(__name__)

router = APIRouter(
    # prefix="/feedback",
    # tags=["feedback"],
    # dependencies=[Depends(security)]
)


@router.post(
    "/",
    responses={
    201: {"model": FeedbackServiceResponse, "description": "Created"},
    401: {"model": ErrorResponse, "description": "Unauthorized"},
    500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
    tags=["feedback"],
    summary= "Submit a new feedback record",
)
async def create_feedback(
    request: Request,
    feedback: FeedbackServiceRequest,
    )->FeedbackServiceResponse:
    """Submit new feedback"""
    logger.info("Incoming headers: %s", request.headers)
    logger.info("Call to create feedback record.")
    return await submit_feedback(feedback)


@router.get(
    "/",
    responses={
        200: {"model": FeedbackServiceRequest, "description": "Success"},
        401: {"model": ErrorResponse, "description": "Unauthorized"},
        404: {"model": ErrorResponse, "description": "Not Found"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
)
async def read_feedback_with_filter(
    filter: Optional[str] = Query(None, description= "JMESPath expression to filter records"),
    limit: int = Query(20, ge=1, le=100, description= "Maximum number of records to return"),
    next_token: Optional[str] = Query(None, description="Pagination token to retrieve next set of records")
)-> Dict[str, Any]:
    """Get feedback by ID"""
    logger.info(
        "Call to retrieve feedback record", 
        extra={"filter": filter, "limit": limit, "next_token": next_token}
    )
    return await get_feedback(filter=filter, limit=limit, next_token=next_token)


@router.get(
    "/{feedback_id}",
    responses={
        200: {"model": FeedbackServiceRequest, "description": "Success"},
        401: {"model": ErrorResponse, "description": "Unauthorized"},
        404: {"model": ErrorResponse, "description": "Not Found"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
)
async def read_feedback(feedback_id: str)->FeedbackServiceRequest:
    """Get feedback by ID"""
    logger.info(
        "Call to retrieve feedback record", 
        extra={feedback_id: feedback_id}
    )
    return await get_feedback_by_id(feedback_id)


@router.delete(
    "/{feedback_id}", 
    responses={
        200: {"model": FeedbackServiceResponse, "description": "Success"},
        401: {"model": ErrorResponse, "description": "Unauthorized"},
        404: {"model": ErrorResponse, "description": "Not Found"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
)
async def remove_feedback(feedback_id: str)->FeedbackServiceResponse:
    """Delete feedback by its ID"""
    logger.info(
        "Call to delete feedback records", 
        extra={"feedback_id": feedback_id}
    )
    return await delete_feedback_by_feedback_id(feedback_id)