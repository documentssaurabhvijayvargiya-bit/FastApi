"""Create phone number for user column

Revision ID: 3054ccde84bf
Revises: 
Create Date: 2026-10-04 22:22:12.687477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3054ccde84bf'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))

def downgrade() -> None:
    op.drop_column('users', 'phone_number')
