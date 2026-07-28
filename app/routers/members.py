from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.member import (
    MemberCreate,
    MemberUpdate,
    MemberResponse
)

from app.repositories.member_repository import (
    create_member,
    get_members,
    get_member_by_id,
    update_member,
    delete_member
)

from app.auth.permissions import require_role


router = APIRouter(
    prefix="/members",
    tags=["Members"]
)


# Create Member
@router.post(
    "/",
    response_model=MemberResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[
        Depends(require_role(["Admin", "Librarian"]))
    ]
)
def add_member(
    member: MemberCreate,
    db: Session = Depends(get_db)
):

    return create_member(
        db,
        member
    )



# Get All Members
@router.get(
    "/",
    response_model=list[MemberResponse]
)
def read_members(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    return get_members(
        db,
        skip,
        limit
    )



# Get Single Member
@router.get(
    "/{member_id}",
    response_model=MemberResponse
)
def read_member(
    member_id: int,
    db: Session = Depends(get_db)
):

    member = get_member_by_id(
        db,
        member_id
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return member



# Update Member
@router.put(
    "/{member_id}",
    response_model=MemberResponse,
    dependencies=[
        Depends(require_role(["Admin", "Librarian"]))
    ]
)
def edit_member(
    member_id: int,
    member: MemberUpdate,
    db: Session = Depends(get_db)
):

    updated_member = update_member(
        db,
        member_id,
        member
    )

    if not updated_member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return updated_member



# Delete Member
@router.delete(
    "/{member_id}",
    dependencies=[
        Depends(require_role(["Admin"]))
    ]
)
def remove_member(
    member_id: int,
    db: Session = Depends(get_db)
):

    deleted_member = delete_member(
        db,
        member_id
    )

    if not deleted_member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return {
        "message": "Member deleted successfully"
    }