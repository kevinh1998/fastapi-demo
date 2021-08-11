import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.utils.enums import DishType


class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    name = Column(String, index=True, unique=True, nullable=False)
    dish_type = Column(Enum(DishType), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    persons = Column(String, nullable=False)
    actions = Column(String, nullable=False)
    url = Column(String, nullable=True)
    ingredients = relationship("RecipeIngredient", back_populates="recipe")
