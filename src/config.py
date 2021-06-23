from dataclasses import dataclass
from typing import List

from yaml import safe_load


with open("./config.yml") as f:
    config = safe_load(f)


@dataclass
class ConfigDatabase:
    host: str = "127.0.0.1"
    port: int = 5432
    password: str = "password"
    user: str = "root"
    database: str = "discordemu"

    @property
    def dsn(self) -> str:
        return f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class ConfigUser:
    id: int
    token: str
    username: str
    discriminator: int


@dataclass
class Config:
    database: ConfigDatabase
    applications: List[ConfigUser]
    host: str


cfg_db = ConfigDatabase(**config["database"])
cfg_apps = [ConfigUser(**app) for app in config["applications"]]

CONFIG = Config(cfg_db, cfg_apps, config["host"])
