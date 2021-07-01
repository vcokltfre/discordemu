from fastapi import APIRouter, WebSocket

from .handler import WebSocketHandler


router = APIRouter()


@router.websocket("/ws")
async def ws_connect(ws: WebSocket) -> None:
    handler = WebSocketHandler(ws)
    await handler.start()
