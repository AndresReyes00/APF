
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/measurements",
    tags=["Measurements"],
)


@router.get("")
def get_measurements():
    return {
        "items": [],
        "total": 0,
        "message": "Measurements endpoint is ready",
    }
