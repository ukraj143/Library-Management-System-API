from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.borrow import (
    BorrowCreate,
    BorrowUpdate,
    BorrowResponse
)

from app.repositories.borrow_repository import (
    create_borrow,
    get_borrows,
    get_borrow_by_id,
    update_borrow,
    delete_borrow,
    get_overdue_borrows
)

from app.auth.permissions import require_role


router = APIRouter(
    prefix="/borrow",
    tags=["Borrow"]
)



# Issue Book
@router.post(
    "/",
    response_model=BorrowResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[
        Depends(require_role(["Admin", "Librarian"]))
    ]
)
def issue_book(
    borrow: BorrowCreate,
    db: Session = Depends(get_db)
):

    new_borrow = create_borrow(
        db,
        borrow
    )

    if not new_borrow:
        raise HTTPException(
            status_code=400,
            detail="Book not available"
        )

    return new_borrow



# Get All Borrow Records
@router.get(
    "/",
    response_model=list[BorrowResponse]
)
def read_borrows(
    db: Session = Depends(get_db)
):

    return get_borrows(db)



# Get Overdue Borrow Records
@router.get(
    "/overdue",
    response_model=list[BorrowResponse]
)
def overdue_books(
    db: Session = Depends(get_db)
):

    return get_overdue_borrows(db)



# Get Single Borrow Record
@router.get(
    "/{borrow_id}",
    response_model=BorrowResponse
)
def read_borrow(
    borrow_id: int,
    db: Session = Depends(get_db)
):

    borrow = get_borrow_by_id(
        db,
        borrow_id
    )

    if not borrow:
        raise HTTPException(
            status_code=404,
            detail="Borrow record not found"
        )

    return borrow



# Return Book / Update Borrow
@router.put(
    "/{borrow_id}",
    response_model=BorrowResponse,
    dependencies=[
        Depends(require_role(["Admin", "Librarian"]))
    ]
)
def return_book(
    borrow_id: int,
    borrow: BorrowUpdate,
    db: Session = Depends(get_db)
):

    updated_borrow = update_borrow(
        db,
        borrow_id,
        borrow
    )

    if not updated_borrow:
        raise HTTPException(
            status_code=404,
            detail="Borrow record not found"
        )

    return updated_borrow



# Delete Borrow Record
@router.delete(
    "/{borrow_id}",
    dependencies=[
        Depends(require_role(["Admin"]))
    ]
)
def remove_borrow(
    borrow_id: int,
    db: Session = Depends(get_db)
):

    deleted_borrow = delete_borrow(
        db,
        borrow_id
    )

    if not deleted_borrow:
        raise HTTPException(
            status_code=404,
            detail="Borrow record not found"
        )

    return {
        "message": "Borrow record deleted successfully"
    }