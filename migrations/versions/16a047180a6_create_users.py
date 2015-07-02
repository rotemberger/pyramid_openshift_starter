"""Create Users

Revision ID: 16a047180a6
Revises: 
Create Date: 2015-07-01 22:06:39.651459

"""

# revision identifiers, used by Alembic.
revision = '16a047180a6'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('password', sa.String(256), nullable=False),
        sa.Column('permission', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('users')