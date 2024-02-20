from backend.api.api_v1.endpoints import generic_endpoints, analysis_endpoints
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(
    generic_endpoints.router,
    tags=["Generic"]
    )
api_router.include_router(
    analysis_endpoints.router,
    tags=["Analysis"]
    )
