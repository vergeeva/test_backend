"""add column

Revision ID: 07b8996f3adc
Revises: b2985e777b27
Create Date: 2023-03-05 16:44:29.084276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07b8996f3adc'
down_revision = 'b2985e777b27'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_clickers', sa.Column('click_count', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'user_clickers', ['click_count'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_clickers', type_='unique')
    op.drop_column('user_clickers', 'click_count')
    # ### end Alembic commands ###
