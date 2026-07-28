from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate



def create_book(
    db: Session,
    book: BookCreate
):

    db_book = Book(
        **book.model_dump()
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book



def get_books(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return (
        db.query(Book)
        .offset(skip)
        .limit(limit)
        .all()
    )



def get_book_by_id(
    db: Session,
    book_id: int
):

    return (
        db.query(Book)
        .filter(Book.id == book_id)
        .first()
    )



def update_book(
    db: Session,
    book_id: int,
    book_data: BookUpdate
):

    db_book = get_book_by_id(
        db,
        book_id
    )

    if not db_book:
        return None


    update_data = book_data.model_dump(
        exclude_unset=True
    )


    for key, value in update_data.items():
        setattr(
            db_book,
            key,
            value
        )


    db.commit()
    db.refresh(db_book)

    return db_book



def delete_book(
    db: Session,
    book_id: int
):

    db_book = get_book_by_id(
        db,
        book_id
    )

    if not db_book:
        return None


    db.delete(db_book)
    db.commit()

    return db_book