"""Added url and enum for dish type

Revision ID: 255cba6780da
Revises: 2daf21703bab
Create Date: 2021-08-11 08:16:59.311936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic
revision = "255cba6780da"
down_revision = "2daf21703bab"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    dish_type = postgresql.ENUM("breakfast", "lunch", "dinner", name="dish_type")
    dish_type.create(op.get_bind())
    op.add_column("recipe", sa.Column("url", sa.String(), nullable=True))
    op.alter_column(
        "recipe",
        "dish_type",
        existing_type=sa.VARCHAR(),
        type_=sa.Enum("breakfast", "lunch", "dinner", name="dish_type"),
        existing_nullable=False,
        postgresql_using="dish_type::dish_type",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "recipe",
        "dish_type",
        existing_type=sa.Enum("breakfast", "lunch", "dinner", name="dish_type"),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    op.drop_column("recipe", "url")
    bind = op.get_bind()
    sa.Enum(name="dish_type").drop(bind, checkfirst=False)
    # ### end Alembic commands ###
