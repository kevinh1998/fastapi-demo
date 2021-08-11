from typing import List, Optional

from app.models.ingredient import IngredientCreate
from app.models.core import CoreModel, IDModelMixin
from app.utils.enums import DishType


class RecipeBase(CoreModel):
    dish_type: DishType
    cooking_time: int
    persons: str
    actions: str
    url: Optional[str] = None
    ingredients: List[IngredientCreate]


class RecipeCreate(RecipeBase):
    pass


class RecipeDB(IDModelMixin, RecipeBase):
    pass
