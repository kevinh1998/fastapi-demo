"""create_main_tables

Revision ID: 2daf21703bab
Revises: 
Create Date: 2021-07-13 13:25:55.068809

"""
from sqlalchemy.sql.schema import ForeignKey
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = "2daf21703bab"
down_revision = None
branch_labels = None
depends_on = None


def create_all_tables() -> None:
    op.create_table(
        "recipe",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("dish_type", sa.String, nullable=False),
        sa.Column("cooking_time", sa.Integer, nullable=False),
        sa.Column("persons", sa.String, nullable=False),
        sa.Column("actions", sa.String, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_recipe_name"), "recipe", ["name"], unique=True)
    op.create_index(op.f("ix_recipe_id"), "recipe", ["id"], unique=True)
    op.create_table(
        "ingredient",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_ingredient_name"), "ingredient", ["name"], unique=True)
    op.create_index(op.f("ix_ingredient_id"), "ingredient", ["id"], unique=True)
    op.create_table(
        "recipe_ingredient",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("value", sa.Numeric(10, 4), nullable=True),
        sa.Column("measure", sa.String, nullable=True),
        sa.Column("recipe_id", sa.Integer, ForeignKey("recipe.id"), nullable=False),
        sa.Column(
            "ingredient_id", sa.Integer, ForeignKey("ingredient.id"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("recipe_id", "ingredient_id", name="uix_recipe_ingredient"),
    )
    op.create_index(
        op.f("ix_recipe_ingredient_id"), "recipe_ingredient", ["id"], unique=True
    )


def upgrade() -> None:
    create_all_tables()


def downgrade() -> None:
    op.drop_index(op.f("ix_recipe_ingredient_id"), table_name="recipe_ingredient")
    op.drop_table("recipe_ingredient")
    op.drop_index(op.f("ix_recipe_name"), table_name="recipe")
    op.drop_index(op.f("ix_recipe_id"), table_name="recipe")
    op.drop_table("recipe")
    op.drop_index(op.f("ix_ingredient_name"), table_name="ingredient")
    op.drop_index(op.f("ix_ingredient_id"), table_name="ingredient")
    op.drop_table("ingredient")
