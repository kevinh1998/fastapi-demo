from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Ingredient(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    name = Column(String, index=True, unique=True, nullable=False)
    recipes = relationship("RecipeIngredient", back_populates="ingredient")
