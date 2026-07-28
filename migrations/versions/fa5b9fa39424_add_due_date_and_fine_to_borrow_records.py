"""add due date and fine to borrow records

Revision ID: fa5b9fa39424
Revises: 1a297cef61fd
Create Date: 2026-07-29 01:54:13.493534

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa5b9fa39424'
down_revision: Union[str, Sequence[str], None] = '1a297cef61fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        'borrow_records',
        sa.Column(
            'due_date',
            sa.Date(),
            nullable=True
        )
    )

    op.add_column(
        'borrow_records',
        sa.Column(
            'fine_amount',
            sa.Float(),
            nullable=True
        )
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        'borrow_records',
        'fine_amount'
    )

    op.drop_column(
        'borrow_records',
        'due_date'
    )
