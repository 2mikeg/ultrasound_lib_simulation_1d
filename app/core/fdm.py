from pyexpat import model
from typing import Dict
import pandas as pd
from core.config.models import ModelsParams
from core.config.config import Settings
import numpy as np

fdm_switcher: Dict = {
    "implicit": 0,
    "explicit": 1
}

def fdm(params_models: ModelsParams) -> np.ndarray:

    database: pd.DataFrame = pd.read_csv(Settings.DB_PATH)

    result = fdm_switcher.get(params_models.fdm_schema, NotImplemented)(
        indexes=params_models.indexes,
        database=database,
        nodes=params_models.nodes,
        n_steps=params_models.n_steps,
        name=params_models.name,
        layer_number=params_models.layer_number,
        save=params_models.save
        )

    return result