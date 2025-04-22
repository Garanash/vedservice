from fastapi import APIRouter
from articles import router as search_router

router = APIRouter()
router.include_router(search_router)
