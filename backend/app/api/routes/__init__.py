from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.recipe import router as recipe_router

router = APIRouter()

router.include_router(health_router, prefix="/health", tags=["health"])
router.include_router(recipe_router, prefix="/recipe", tags=["recipes"])
