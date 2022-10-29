from core.config.models import ModelsParams
from core.fdm import fdm


params = ModelsParams(
    fdm_schema="explicit",
    indexes=[0, 11],
    layer_number=4,
    nodes=150,
    n_steps=600,
    name="file",
    save=True
)

matrix_result = fdm(params)