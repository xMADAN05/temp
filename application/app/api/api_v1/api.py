"""
API router configuration module.

This module defines the main API router and registers all endpoint routers
for the application's REST API.
"""

from fastapi import APIRouter 

from app.api.api_v1.endpoints import feedback

api_router = APIRouter()

api_router.include_router(feedback.router,
                        #   prefix="/feedback",
                          tags=["feedback"])