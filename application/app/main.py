
import logging

from fastapi import FastAPI, Request
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.utils.common_utils import openapi_spec

# logging.config.dictConfig(logging_config)

logger = logging.getLogger(__name__)

logger.info("Application starting")

def generate_unique_route_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}" 

app = FastAPI(
    title= settings.project_name,
    # openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    generate_unique_id_function= generate_unique_route_id,
    docs_url=f"{settings.api_v1_prefix}/docs",
    redoc_url=f"{settings.api_v1_prefix}/redoc",
)


# if openapi_spec:
#     app.openapi_schema = openapi_spec

# app.add_middleware(Request)

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthcheck", tags=["healthcheck"])
def get_healthcheck_response():
    """Default Heathcheck endpoint"""
    logger.debug("Healthcheck")
    response = {"success": True}
    return response

app.include_router(api_router ,prefix=settings.api_v1_prefix)


logger.info("Application started")
