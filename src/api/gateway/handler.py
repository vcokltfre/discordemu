from asyncio import TimeoutError, get_running_loop, wait_for

from fastapi import WebSocket


class WebSocketHandler:
    def __init__(self, ws: WebSocket) -> None:
        self.ws = ws

        self.seq = None

        self.loop = get_running_loop()

    async def send(self, data: dict) -> None:
        _data = {
            "op": None,
            "d": None,
            "t": None,
            "s": None,
        }
        _data.update(data)
        await self.ws.send_json(_data)

    async def _read(self) -> None:
        async for message in self.ws.iter_json():
            op = message.get("op")
            d = message.get("d")
            t = message.get("t")
            s = message.get("s")

            if op == 1:
                self.loop.create_task(self.send({"op": 11}))
            elif op == 2:
                await self.send({"op":0, "t": "READY", "d": {}})  # TODO: Flesh out ready

            # TODO: Implement other ops

    async def start(self) -> None:
        await self.ws.accept()

        # Hello
        await self.ws.send_json({
            "op": 10,
            "d": {
                "heartbeat_interval": 45000
            }
        })

        await self._read()

