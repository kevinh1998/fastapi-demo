from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.orm import relationship

from base import Base


class RecipeIngredient(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    value = Column(Numeric(10, 4), nullable=True)
    measure = Column(String, nullable=True)
    recipe_id = Column(Integer, ForeignKey("recipe.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredient.id"), nullable=False)
    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")
    __table_args__ = (
        UniqueConstraint("recipe_id", "ingredient_id", name="uix_recipe_ingredient"),
    )
