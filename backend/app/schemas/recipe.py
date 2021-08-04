from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    name = Column(String, index=True, unique=True, nullable=False)
    dish_type = Column(String, nullable=False)
    cooking_time = Column(Integer, nullable=False)
    persons = Column(String, nullable=False)
    actions = Column(String, nullable=False)
    ingredients = relationship("RecipeIngredient", back_populates="recipe")
