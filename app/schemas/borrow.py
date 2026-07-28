from pydantic import BaseModel
from datetime import date
from typing import Optional


class BorrowCreate(BaseModel):

    member_id: int
    book_id: int
    issue_date: date
    due_date: Optional[date] = None



class BorrowUpdate(BaseModel):
    due_date: Optional[date] = None

    return_date: Optional[date] = None
    status: Optional[str] = None
    fine_amount: Optional[float] = None



class BorrowResponse(BaseModel):

    id: int

    member_id: int
    book_id: int

    issue_date: date
    due_date: Optional[date] = None

    return_date: Optional[date] = None

    status: str

    fine_amount: Optional[float] = 0


    class Config:
        from_attributes = True