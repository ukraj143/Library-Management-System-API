from sqlalchemy import Column, Integer, Date, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class BorrowRecord(Base):

    __tablename__ = "borrow_records"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    member_id = Column(
        Integer,
        ForeignKey("members.id"),
        nullable=False
    )

    book_id = Column(
        Integer,
        ForeignKey("books.id"),
        nullable=False
    )

    issue_date = Column(
        Date,
        nullable=False
    )

    due_date = Column(
        Date,
        nullable=False
    )

    return_date = Column(
        Date,
        nullable=True
    )

    status = Column(
        String,
        default="Issued"
    )

    fine_amount = Column(
        Float,
        default=0
    )


    member = relationship(
        "Member"
    )

    book = relationship(
        "Book"
    )