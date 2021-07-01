from fastapi import APIRouter

from src.config import CONFIG
from src.models.api.gateway import GetGateway, GetGatewayBot, SessionStartLimit


router = APIRouter(prefix="/gateway")


@router.get("")
async def get_gateway() -> GetGateway:
    return GetGateway(url=f"ws://{CONFIG.host}/ws")


@router.get("/bot")
async def get_gateway_bot() -> GetGatewayBot:
    session_start_limit = SessionStartLimit(
        total=1000,
        remaining=999,
        reset_after=14400000,
        max_concurrency=1,
    )

    return GetGatewayBot(
        url=f"ws://{CONFIG.host}/ws",
        shards=1,  # TODO: Some sort of sharding logic
        session_start_limit=session_start_limit,
    )
