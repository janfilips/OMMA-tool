import logging
from typing import Dict

from backend.utils.logging_utils import log_endpoint
from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/xxx-todo")
@log_endpoint
async def xxx_analysis_endpoints_todo() -> Dict[str, str]:
    """Health check endpoint."""
    return {
        "status": "XXX",
        "message": "Working on this currenctly",
    }
