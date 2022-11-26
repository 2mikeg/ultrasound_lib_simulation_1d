from typing import List

from pydantic import BaseModel

from app.core.config.config import FDMSchemas


class ModelsParams(BaseModel):
    fdm_schema: FDMSchemas
    indexes: List[int]
    nodes: int
    n_steps: int
    name: str
    layer_number: int
    save: bool
    geometric_unit: List[int]
