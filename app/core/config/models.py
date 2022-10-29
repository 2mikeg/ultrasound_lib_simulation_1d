from typing import List, Optional
from pydantic import BaseModel

class ModelsParams(BaseModel):
    fdm_schema: str
    indexes: List
    nodes: int
    n_steps: int
    name: str
    layer_number: int
    save: bool