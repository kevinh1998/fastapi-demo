from typing import Optional

from app.models.core import CoreModel, IDModelMixin


class IngredientBase(CoreModel):
    value: Optional[float]
    measure: Optional[str]


class IngredientCreate(IngredientBase):
    pass


class IngredientDB(IDModelMixin, IngredientBase):
    pass
