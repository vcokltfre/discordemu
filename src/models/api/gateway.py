from pydantic import BaseModel


class GetGateway(BaseModel):
    url: str


class SessionStartLimit(BaseModel):
    total: int
    remaining: int
    reset_after: int
    max_concurrency: int


class GetGatewayBot(BaseModel):
    url: str
    shards: int
    session_start_limit: SessionStartLimit
