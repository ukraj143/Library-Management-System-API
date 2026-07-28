# 📚 Library Management System API

A complete backend Library Management System developed using **FastAPI**, **PostgreSQL**, and **SQLAlchemy ORM**.
This project provides RESTful APIs for managing books, members, borrowing operations, authentication, and authorization with role-based access control.

The system is designed with a scalable backend architecture following separation of concerns using:

* Router Layer
* Schema Layer
* Repository Layer
* Database Layer
* Authentication Layer

---

# 🚀 Project Overview

The Library Management System allows libraries to digitally manage their complete workflow.

The application provides functionality for:

* User authentication and authorization
* Managing library books
* Managing members
* Issuing books
* Returning books
* Tracking overdue books
* Automatic fine calculation
* Role-based permissions

The project follows modern backend development practices with secure authentication, database management, and clean API architecture.

---

# ✨ Key Features

## 🔐 Authentication & Authorization

The application implements secure authentication using JWT tokens.

Features:

* User registration
* User login
* JWT token generation
* Protected API routes
* Role-based access control

Supported roles:

### Admin

Admin has complete access:

* Manage users
* Manage books
* Manage members
* Delete records
* Access all library operations

### Librarian

Librarian can:

* Add books
* Update books
* Issue books
* Accept returned books
* Manage borrow records

### Member

Members can:

* View available books
* View borrowing information

---

# 📖 Book Management

The Book Management module handles all operations related to library books.

Features:

* Add new books
* View all books
* View individual book details
* Update book information
* Delete books
* Track available copies

Book information includes:

* Title
* Author
* Category
* ISBN
* Total copies
* Available copies

---

# 👥 Member Management

The Member Management module handles library members.

Features:

* Create members
* View members
* Update member information
* Delete members

Member information includes:

* Name
* Email
* Phone number
* Membership details

---

# 📚 Borrow Management

The Borrow module manages complete book issuing and returning workflow.

Features:

## Issue Book

When a book is issued:

* Borrow record is created
* Available book copies are reduced
* Status changes to "Issued"

## Return Book

When a book is returned:

* Return date is updated
* Available copies increase
* Status changes to "Returned"

## Fine Calculation

The system automatically calculates fines.

Fine calculation:

```
Fine = Late Days × ₹10
```

Example:

If a book is returned 5 days late:

```
Fine = 5 × ₹10

Total Fine = ₹50
```

---

# ⏰ Overdue Book Tracking

The system provides an overdue API to identify books that are not returned before the due date.

A book is considered overdue when:

* Due date is completed
* Return date is empty
* Status is still "Issued"

Example:

```
GET /borrow/overdue
```

Response provides all overdue borrow records.

---

# 🛠️ Technology Stack

## Backend Framework

### FastAPI

Used for:

* Creating REST APIs
* Request validation
* Dependency injection
* Automatic Swagger documentation

## Programming Language

### Python

Used for:

* Backend development
* Business logic
* Database operations

## Database

### PostgreSQL

Used for:

* Storing application data
* Managing relationships
* Persistent storage

## ORM

### SQLAlchemy

Used for:

* Database models
* Query operations
* Database abstraction

## Authentication

### JWT Authentication

Used for:

* Secure user sessions
* Protected API access

Libraries:

* python-jose
* passlib
* bcrypt

## Database Migration

### Alembic

Used for:

* Managing database schema changes
* Version control of database structure

---

# 🏗️ Project Architecture

The application follows a layered architecture.

```
Client
  |
  |
FastAPI Router Layer
  |
  |
Schema Validation Layer
  |
  |
Repository Layer
  |
  |
SQLAlchemy ORM
  |
  |
PostgreSQL Database
```

---

# 📂 Project Structure

```
LibraryManagementSystem

│
├── app
│   │
│   ├── auth
│   │   ├── hashing.py
│   │   ├── oauth2.py
│   │   └── permissions.py
│   │
│   ├── models
│   │   ├── user.py
│   │   ├── book.py
│   │   ├── member.py
│   │   └── borrow.py
│   │
│   ├── schemas
│   │   ├── user.py
│   │   ├── book.py
│   │   ├── member.py
│   │   └── borrow.py
│   │
│   ├── repositories
│   │   ├── user_repository.py
│   │   ├── book_repository.py
│   │   ├── member_repository.py
│   │   └── borrow_repository.py
│   │
│   ├── routers
│   │   ├── auth.py
│   │   ├── books.py
│   │   ├── members.py
│   │   └── borrow.py
│   │
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── migrations
│
├── uploads
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# 📁 File Responsibilities

## main.py

Application entry point.

Responsibilities:

* Create FastAPI application
* Register routers
* Configure application settings

## database.py

Database connection management.

Responsibilities:

* Create SQLAlchemy engine
* Create database sessions
* Provide database dependency

## models/

Contains database table definitions.

Example:

* User model
* Book model
* Member model
* Borrow model

## schemas/

Contains request and response validation models.

Responsibilities:

* Validate incoming data
* Define API response format

## repositories/

Contains database operations.

Responsibilities:

* Create records
* Fetch records
* Update records
* Delete records

## routers/

Contains API endpoints.

Responsibilities:

* Handle HTTP requests
* Call repository functions
* Return responses

## auth/

Contains authentication logic.

Includes:

* Password hashing
* JWT token creation
* Permission validation

---

# ⚙️ Installation Guide

## Step 1: Clone Repository

```bash
git clone <repository-url>

cd LibraryManagementSystem
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create `.env` file:

```
DATABASE_URL=postgresql://localhost:5432/library_management

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# 🗄️ Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE library_management;
```

Run migrations:

```bash
alembic upgrade head
```

---

# ▶️ Running Application

Start server:

```bash
uvicorn app.main:app --reload
```

Application URL:

```
http://127.0.0.1:8000
```

---

# 📘 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

FastAPI automatically generates interactive API documentation.

---

# 🔗 API Endpoints

## Authentication

| Method | Endpoint     | Description   |
| ------ | ------------ | ------------- |
| POST   | /auth/signup | Register user |
| POST   | /auth/login  | Login user    |

---

## Books

| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| POST   | /books      | Create book |
| GET    | /books      | Get books   |
| GET    | /books/{id} | Get book    |
| PUT    | /books/{id} | Update book |
| DELETE | /books/{id} | Delete book |

---

## Members

| Method | Endpoint      | Description   |
| ------ | ------------- | ------------- |
| POST   | /members      | Create member |
| GET    | /members      | Get members   |
| GET    | /members/{id} | Get member    |
| PUT    | /members/{id} | Update member |
| DELETE | /members/{id} | Delete member |

---

## Borrow

| Method | Endpoint        | Description        |
| ------ | --------------- | ------------------ |
| POST   | /borrow         | Issue book         |
| GET    | /borrow         | Get borrow records |
| GET    | /borrow/{id}    | Get borrow record  |
| PUT    | /borrow/{id}    | Return book        |
| DELETE | /borrow/{id}    | Delete record      |
| GET    | /borrow/overdue | Get overdue books  |

---

# 🧪 Testing

All APIs were tested using Swagger UI.

Testing covered:

✅ User registration
✅ User login
✅ JWT authentication
✅ Role authorization
✅ Book CRUD operations
✅ Member CRUD operations
✅ Borrow workflow
✅ Return workflow
✅ Fine calculation
✅ Overdue tracking
✅ Error handling

---

# 🔒 Security Implementation

The application implements:

* Password hashing using bcrypt
* JWT token authentication
* Protected routes
* Role-based permissions
* Environment variable configuration

---

# 🚧 Future Enhancements

Possible improvements:

* Email notifications for overdue books
* Book reservation system
* Dashboard analytics
* Docker deployment
* Cloud deployment
* Automated unit testing
* Redis caching
* Background notification service

---

# 👨‍💻 Developer

**Uday Kiran**

Backend Developer

---

# 📌 Conclusion

This Library Management System demonstrates a complete backend application using FastAPI with authentication, authorization, database management, and scalable architecture.

The project follows industry-standard practices and can be extended for real-world library management requirements.
