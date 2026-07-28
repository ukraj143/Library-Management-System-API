from sqlalchemy.orm import Session

from app.models.user import User


def get_user_by_email(
    db: Session,
    email: str
):
    return db.query(User).filter(
        User.email == email
    ).first()



def create_user(
    db: Session,
    user_data
):

    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password=user_data.password,
        role=user_data.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user