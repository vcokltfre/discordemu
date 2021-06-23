from fastapi import APIRouter

from .gateway import router as gateway_router


router = APIRouter(prefix="/api")

router.include_router(gateway_router)
