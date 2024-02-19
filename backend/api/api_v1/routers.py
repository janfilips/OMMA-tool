from backend.api.api_v1.endpoints import generic_endpoints
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(
    generic_endpoints.router,
    tags=["Generic"]
    )
