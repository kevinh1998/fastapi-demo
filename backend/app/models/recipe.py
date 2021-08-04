from typing import List

from app.models.ingredient import IngredientCreate
from app.models.core import CoreModel, IDModelMixin


class RecipeBase(CoreModel):
    dish_type: str
    cooking_time: int
    persons: str
    actions: str
    ingredients: List[IngredientCreate]


class RecipeCreate(RecipeBase):
    pass


class RecipeDB(IDModelMixin, RecipeBase):
    pass
