from typing import Dict

import numpy as np
import pandas as pd
from core.config.config import Settings
from core.models.model_params import ModelsParams
from explicit.explicit_method import fdm_explicit
from implicit.implicit_method import fdm_implicit

from app.core.config.config import FDMSchemas

fdm_switcher: Dict = {
    FDMSchemas.Implicit.value: fdm_implicit,
    FDMSchemas.Explicit.value: fdm_explicit,
}


def fdm(params_models: ModelsParams) -> np.ndarray:

    database: pd.DataFrame = pd.read_csv(Settings.DB_PATH)

    result = fdm_switcher.get(params_models.fdm_schema.value, NotImplemented)(
        indexes=params_models.indexes,
        database=database,
        nodes=params_models.nodes,
        n_steps=params_models.n_steps,
        name=params_models.name,
        layer_number=params_models.layer_number,
        save=params_models.save,
    )

    return result
