from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):

    title: str
    isbn: str
    author: str
    publisher: Optional[str] = None
    category: Optional[str] = None
    language: Optional[str] = None
    published_year: Optional[int] = None
    total_copies: int = 1
    available_copies: int = 1
    shelf_location: Optional[str] = None



class BookCreate(BookBase):
    pass



class BookUpdate(BaseModel):

    title: Optional[str] = None
    isbn: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    category: Optional[str] = None
    language: Optional[str] = None
    published_year: Optional[int] = None
    total_copies: Optional[int] = None
    available_copies: Optional[int] = None
    shelf_location: Optional[str] = None



class BookResponse(BookBase):

    id: int

    class Config:
        from_attributes = True