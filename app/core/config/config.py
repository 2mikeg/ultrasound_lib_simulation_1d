from pydantic import BaseSettings

class Conf(BaseSettings):
    DB_PATH: str = "app/core/database/materials_properties.csv"

Settings = Conf()
