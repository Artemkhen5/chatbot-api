from fastapi import APIRouter

from src.api.endpoints import llm

router = APIRouter()
router.include_router(llm.router)
