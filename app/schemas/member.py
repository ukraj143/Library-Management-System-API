from pydantic import BaseModel
from datetime import date
from typing import Optional

class MemberBase(BaseModel):

    full_name: str
    email: str
    phone_number: Optional[str] = None
    membership_id: str
    address: Optional[str] = None
    membership_date: Optional[date] = None
    status: str = "Active"



class MemberCreate(MemberBase):
    pass



class MemberUpdate(BaseModel):

    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
status: Optional[str] = None


class MemberResponse(MemberBase):

    id: int

    class Config:
        from_attributes = True