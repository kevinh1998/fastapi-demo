from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED
from sqlalchemy.orm import sessionmaker

from app.models.recipe import RecipeCreate, RecipeDB
from app.repositories.recipe import RecipeRepository
from app.api.deps import get_repository

router = APIRouter()


@router.post(
    "/",
    response_model=RecipeCreate,
    name="recipe: create_recipe",
    status_code=HTTP_201_CREATED,
)
async def create_recipe(
    *,
    recipe_repo: RecipeRepository = Depends(get_repository(RecipeRepository)),
    recipe_in: RecipeCreate,
) -> RecipeCreate:
    recipe = await recipe_repo.create_recipe(recipe_in=recipe_in)
    if not recipe:
        raise HTTPException(status_code=409, detail="Recipe name already exists")
    return recipe


@router.get("/", response_model=List[RecipeCreate], name="recipe: get_recipes")
async def get_recipes(
    recipe_repo: RecipeRepository = Depends(get_repository(RecipeRepository)),
):
    return await recipe_repo.get_recipes()


@router.get("/{name}", response_model=RecipeCreate, name="recipe: get_recipe_by_name")
async def get_recipe(
    *,
    recipe_repo: RecipeRepository = Depends(get_repository(RecipeRepository)),
    name: str,
):
    recipe = await recipe_repo.get_recipe(name=name)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
