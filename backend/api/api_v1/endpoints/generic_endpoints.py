import logging
from typing import Dict

from backend.utils.logging_utils import log_endpoint
from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/health")
@log_endpoint
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {
        "status": "OK",
        "message": "Application is healthy",
    }
