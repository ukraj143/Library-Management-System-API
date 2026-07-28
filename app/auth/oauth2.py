from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import jwt

from app.database import get_db
from app.config import SECRET_KEY, ALGORITHM
from app.repositories.user_repository import get_user_by_email


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


    user = get_user_by_email(
        db,
        email
    )


    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    return user