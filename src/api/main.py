from asyncpg import Pool, create_pool
from fastapi import FastAPI

from src.api.routers import router
from src.api.gateway import router as gateway_router
from src.config import CONFIG


app = FastAPI(openapi_url=None)
app.include_router(router)
app.include_router(gateway_router)

pool: Pool


@app.on_event("startup")
async def on_startup() -> None:
    """Initialise require components on startup."""

    global pool
    pool = await create_pool(dsn=CONFIG.database.dsn)


@app.on_event("shutdown")
async def on_shutdown() -> None:
    """Gracefully shutdown components."""

    await pool.close()
