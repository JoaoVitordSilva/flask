"""empty message

Revision ID: b8883f6240c9
Revises: c5496fa1776c
Create Date: 2024-05-21 11:35:19.823571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8883f6240c9'
down_revision = 'c5496fa1776c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comentario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('texto', sa.String(), nullable=False))
        batch_op.drop_column('text')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comentario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('texto')

    # ### end Alembic commands ###
