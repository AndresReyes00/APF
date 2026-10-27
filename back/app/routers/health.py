
from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["Health"],
)


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Space Health API is running",
    }