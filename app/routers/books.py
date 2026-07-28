from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.book import (
    BookCreate,
    BookUpdate,
    BookResponse
)

from app.repositories.book_repository import (
    create_book,
    get_books,
    get_book_by_id,
    update_book,
    delete_book
)

from app.auth.permissions import require_role


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


# Add Book
@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[
        Depends(require_role(["Admin", "Librarian"]))
    ]
)
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):

    return create_book(
        db,
        book
    )



# Get All Books
@router.get(
    "/",
    response_model=list[BookResponse]
)
def read_books(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    return get_books(
        db,
        skip,
        limit
    )



# Get Single Book
@router.get(
    "/{book_id}",
    response_model=BookResponse
)
def read_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    book = get_book_by_id(
        db,
        book_id
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book



# Update Book
@router.put(
    "/{book_id}",
    response_model=BookResponse,
    dependencies=[
        Depends(require_role(["Admin", "Librarian"]))
    ]
)
def edit_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db)
):

    updated_book = update_book(
        db,
        book_id,
        book
    )

    if not updated_book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return updated_book



# Delete Book
@router.delete(
    "/{book_id}",
    dependencies=[
        Depends(require_role(["Admin"]))
    ]
)
def remove_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    deleted_book = delete_book(
        db,
        book_id
    )

    if not deleted_book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "message": "Book deleted successfully"
    }