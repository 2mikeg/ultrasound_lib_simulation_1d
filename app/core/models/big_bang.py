from pydantic import BaseModel
from typing import Optional, List, Dict
import numpy as np


class BigBang(BaseModel):
    x: np.ndarray
    interphase_position: List[int]
    e_modulus: Dict
    materials_summary: List
    phi_map: Optional[List] = None
    gamma_map: Optional[List] = None
