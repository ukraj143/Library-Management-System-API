from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.oauth2 import get_current_user
from app.database import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
    Token
)

from app.repositories.user_repository import (
    create_user,
    get_user_by_email
)

from app.auth.hashing import (
    hash_password,
    verify_password
)

from app.auth.jwt_handler import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# REGISTER USER
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    user.password = hash_password(
        user.password
    )


    return create_user(
        db,
        user
    )



# LOGIN USER (OAuth2 Compatible)
@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = get_user_by_email(
        db,
        form_data.username
    )


    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    if not verify_password(
        form_data.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }



# GET CURRENT USER PROFILE
@router.get(
    "/profile",
    response_model=UserResponse
)
def profile(
    current_user = Depends(get_current_user)
):

    return current_user