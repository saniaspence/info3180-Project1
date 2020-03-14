"""empty message

Revision ID: 50107cc51a22
Revises: e3f350267e8a
Create Date: 2020-03-01 19:51:26.983659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50107cc51a22'
down_revision = 'e3f350267e8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###