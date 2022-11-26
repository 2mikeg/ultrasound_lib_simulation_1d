from typing import List

import pandas as pd

from app.core.battery_structure import battery_structure


def fdm_explicit(
    indexes: List,
    database: pd.DataFrame,
    nodes: int,
    n_steps: int,
    name: str,
    layer_number: int,
    save=False,
):

    battery_map = battery_structure(indexes=indexes, layer_number=layer_number)

    