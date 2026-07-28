from sqlalchemy import Column, Integer, String
from app.database import Base


class Book(Base):

    __tablename__ = "books"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    isbn = Column(
        String,
        unique=True,
        nullable=False
    )

    author = Column(
        String,
        nullable=False
    )

    publisher = Column(
        String
    )

    category = Column(
        String
    )

    language = Column(
        String
    )

    published_year = Column(
        Integer
    )

    total_copies = Column(
        Integer,
        default=1
    )

    available_copies = Column(
        Integer,
        default=1
    )

    shelf_location = Column(
        String
    )