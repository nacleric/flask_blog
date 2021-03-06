"""actual post model improved

Revision ID: d1fb66c4a7b3
Revises: 62d69e8c9126
Create Date: 2018-02-12 17:51:36.119489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1fb66c4a7b3'
down_revision = '62d69e8c9126'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('intro', sa.String(), nullable=True))
    op.add_column('post', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'title')
    op.drop_column('post', 'intro')
    # ### end Alembic commands ###
