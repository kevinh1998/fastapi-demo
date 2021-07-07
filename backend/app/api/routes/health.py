from fastapi import APIRouter
from typing import Dict

router = APIRouter()

@router.get("/")
async def get_health() -> Dict[str, str]:
    return {"Health": "OK!"}