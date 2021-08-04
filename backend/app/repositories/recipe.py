from typing import List, Optional

from sqlalchemy.orm import sessionmaker, selectinload
from sqlalchemy.future import select

from app.repositories.base import BaseRepository
from app.models.recipe import RecipeCreate
from app.models.ingredient import IngredientCreate
from app.schemas.recipe import Recipe as RecipeSchema
from app.schemas.ingredient import Ingredient as IngredientSchema
from app.schemas.recipe_ingredient import RecipeIngredient as RecipeIngredientSchema


class RecipeRepository(BaseRepository):
    async def create_recipe(self, *, recipe_in: RecipeCreate) -> RecipeCreate:
        async with self.session() as session:
            recipe = RecipeSchema(
                name=recipe_in.name,
                dish_type=recipe_in.dish_type,
                cooking_time=recipe_in.cooking_time,
                persons=recipe_in.persons,
                actions=recipe_in.actions,
            )
            async with session.begin():
                ingredients = []
                for i in recipe_in.ingredients:
                    ingredient = IngredientSchema(name=i.name)
                    ingredients.append(ingredient)
                    recipe_ingredient = RecipeIngredientSchema(
                        value=i.value, measure=i.measure
                    )
                    recipe_ingredient.ingredient = ingredient
                    recipe.ingredients.append(recipe_ingredient)
                session.add_all(ingredients)

            async with session.begin():
                session.add(recipe)
        return recipe_in

    async def get_recipes(self) -> List[RecipeCreate]:
        recipes = []
        async with self.session() as session:
            stmt = select(RecipeSchema).options(
                selectinload(RecipeSchema.ingredients).selectinload(
                    RecipeIngredientSchema.ingredient
                )
            )
            result = await session.execute(stmt)
            for r in result.scalars():
                ingredients = []
                for i in r.ingredients:
                    ingredients.append(
                        IngredientCreate(
                            name=i.ingredient.name, value=i.value, measure=i.measure
                        )
                    )
                recipes.append(
                    RecipeCreate(
                        name=r.name,
                        dish_type=r.dish_type,
                        cooking_time=r.cooking_time,
                        persons=r.persons,
                        actions=r.actions,
                        ingredients=ingredients,
                    )
                )
        return recipes

    async def get_recipe(self, *, name: str) -> Optional[RecipeCreate]:
        async with self.session() as session:
            stmt = (
                select(RecipeSchema)
                .options(
                    selectinload(RecipeSchema.ingredients).selectinload(
                        RecipeIngredientSchema.ingredient
                    )
                )
                .filter_by(name=name)
            )
            result = await session.execute(stmt)
            recipe = result.scalars().first()
            if not recipe:
                return None
            ingredients = []
            for i in recipe.ingredients:
                ingredients.append(
                    IngredientCreate(
                        name=i.ingredient.name, value=i.value, measure=i.measure
                    )
                )
            return RecipeCreate(
                name=recipe.name,
                dish_type=recipe.dish_type,
                cooking_time=recipe.cooking_time,
                persons=recipe.persons,
                actions=recipe.actions,
                ingredients=ingredients,
            )
