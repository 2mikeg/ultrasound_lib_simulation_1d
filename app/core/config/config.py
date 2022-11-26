from enum import Enum

from pydantic import BaseSettings


class Materials(Enum):
    CATHODE_80_PERCENT = 8


class FDMSchemas(Enum):
    Explicit = "explicit"
    Implicit = "implicit"


class Conf(BaseSettings):
    DB_PATH: str = "app/core/database/materials_properties.csv"


Settings = Conf()
