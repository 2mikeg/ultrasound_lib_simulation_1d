from core.config.config import FDMSchemas, Materials
from core.fdm import fdm
from core.models.model_params import ModelsParams

params = ModelsParams(
    fdm_schema=FDMSchemas.Explicit,
    indexes=[1, 2, 3],
    layer_number=4,
    geometric_unit=[1, 2, 3, 2, 1],
    nodes=150,
    n_steps=600,
    name="file",
    save=True,
)

matrix_result = fdm(params)
