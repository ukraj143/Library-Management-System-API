from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Member(Base):

    __tablename__ = "members"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    phone_number = Column(
        String
    )

    membership_id = Column(
        String,
        unique=True,
        nullable=False
    )

    address = Column(
        String
    )

    membership_date = Column(
        Date
    )

    status = Column(
        String,
        default="Active"
    )