"""Edited models to be able to add photos

Revision ID: a30900dcffb0
Revises: 759091c78bd5
Create Date: 2018-02-12 23:48:45.046850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a30900dcffb0'
down_revision = '759091c78bd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_photos',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('photos')
    op.add_column('blogs', sa.Column('p_author', sa.String(), nullable=True))
    op.add_column('blogs', sa.Column('p_body', sa.String(), nullable=True))
    op.drop_column('blogs', 'q_body')
    op.drop_column('blogs', 'q_author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('q_author', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('q_body', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('blogs', 'p_body')
    op.drop_column('blogs', 'p_author')
    op.create_table('photos',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('pic_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='photos_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='photos_pkey')
    )
    op.drop_table('profile_photos')
    # ### end Alembic commands ###