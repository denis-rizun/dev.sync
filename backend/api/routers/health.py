from fastapi import APIRouter

health_router = APIRouter(tags=["Health"])


@health_router.get(path="/health/", response_model=None, status_code=204)
async def health() -> None:
    return None
