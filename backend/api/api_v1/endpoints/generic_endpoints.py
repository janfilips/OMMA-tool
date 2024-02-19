import logging
from typing import Dict

from backend.core.auth import get_current_user
from backend.db.schemas.user_schema import UserSchema
from backend.utils.logging_utils import log_endpoint
from fastapi import APIRouter, Depends

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
