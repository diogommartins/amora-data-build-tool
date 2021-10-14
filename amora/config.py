from pathlib import Path

from pydantic import BaseSettings

ROOT_PATH = Path(__file__).parent.parent
AMORA_MODULE_PATH = ROOT_PATH.joinpath("amora")


class Settings(BaseSettings):
    TARGET_PROJECT: str
    TARGET_SCHEMA: str
    TARGET_PATH: str = AMORA_MODULE_PATH.joinpath("target").as_posix()
    DBT_MODELS_PATH: str = ROOT_PATH.joinpath("dbt/models").as_posix()

    class Config:
        env_prefix = "AMORA_"


settings = Settings()
