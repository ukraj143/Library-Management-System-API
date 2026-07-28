from fastapi import FastAPI

from app.routers import auth
from app.routers import books
from app.routers import members
from app.routers import borrow


app = FastAPI(
    title="Library Management System API",
    version="1.0.0"
)


app.include_router(
    auth.router
)

app.include_router(
    books.router
)

app.include_router(
    members.router
)

app.include_router(
    borrow.router
)


@app.get("/")
def root():
    return {
        "message": "Library Management System API is Running"
    }