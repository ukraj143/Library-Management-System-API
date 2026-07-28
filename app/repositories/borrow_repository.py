from sqlalchemy.orm import Session
from datetime import date

from app.models.borrow import BorrowRecord
from app.models.book import Book

from app.schemas.borrow import (
    BorrowCreate,
    BorrowUpdate
)



def create_borrow(
    db: Session,
    borrow: BorrowCreate
):

    book = db.query(Book).filter(
        Book.id == borrow.book_id
    ).first()

    if not book:
        return None


    if book.available_copies <= 0:
        return None


    new_borrow = BorrowRecord(
        member_id=borrow.member_id,
        book_id=borrow.book_id,
        issue_date=borrow.issue_date,
        due_date=borrow.due_date,
        status="Issued",
        fine_amount=0
    )


    book.available_copies -= 1


    db.add(new_borrow)

    db.commit()

    db.refresh(new_borrow)

    return new_borrow





def get_borrows(
    db: Session
):

    return db.query(
        BorrowRecord
    ).all()





def get_borrow_by_id(
    db: Session,
    borrow_id: int
):

    return db.query(
        BorrowRecord
    ).filter(
        BorrowRecord.id == borrow_id
    ).first()





def update_borrow(
    db: Session,
    borrow_id: int,
    borrow: BorrowUpdate
):

    db_borrow = get_borrow_by_id(
        db,
        borrow_id
    )


    if not db_borrow:
        return None



    # Update due date
    if borrow.due_date:
        db_borrow.due_date = borrow.due_date



    # Return book
    if borrow.return_date:

        book = db.query(Book).filter(
            Book.id == db_borrow.book_id
        ).first()


        if book:
            book.available_copies += 1



        db_borrow.return_date = borrow.return_date



        # Fine calculation
        if db_borrow.due_date:

            late_days = (
                borrow.return_date - db_borrow.due_date
            ).days


            if late_days > 0:
                db_borrow.fine_amount = late_days * 10
            else:
                db_borrow.fine_amount = 0



    # Update status
    if borrow.status:
        db_borrow.status = borrow.status



    # Manual fine update
    if borrow.fine_amount is not None:
        db_borrow.fine_amount = borrow.fine_amount



    db.commit()

    db.refresh(db_borrow)

    return db_borrow





def delete_borrow(
    db: Session,
    borrow_id: int
):

    db_borrow = get_borrow_by_id(
        db,
        borrow_id
    )


    if not db_borrow:
        return None


    db.delete(db_borrow)

    db.commit()


    return db_borrow





def get_overdue_borrows(
    db: Session
):

    return db.query(
        BorrowRecord
    ).filter(
        BorrowRecord.due_date < date.today(),
        BorrowRecord.return_date == None,
        BorrowRecord.status == "Issued"
    ).all()