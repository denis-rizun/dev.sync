from fastapi import APIRouter

health_router = APIRouter(tags=["health"])


@health_router.get(path="/", response_model=None, status_code=204)
async def health() -> None:
    return None
