# Library Management System API

A RESTful **Library Management System API** built with **Django & Django Rest Framework (DRF)**.  
The API allows managing books, users, and book checkout/return operations, with authentication, pagination, and production deployment.

---

#  Project Overview

This project was developed using a **5-week structured plan**, focusing on clean architecture, real-world API logic, and production readiness.

---

# 🛠 Tech Stack

- Python  
- Django  
- Django REST Framework  
- JWT Authentication  
- SQLite / PostgreSQL  
- Gunicorn  
- PythonAnywhere (Deployment)

---

# 🗂 Project Structure

Library-Management-System/
│
├── library_api/ # Django project settings
├── library/ # Main app (books, users, checkout)
├── manage.py
├── requirements.txt
└── README.md


# 📅 Development Timeline

# ✅ Week 1: Setup & Basic Models

- Created Django project and app
- Set up virtual environment
- Installed Django Rest Framework
- Created core models:
  - User
  - Book
  - Checkout
- Ran migrations
- Tested models using Django shell

*Outcome*
- ✔ Database schema ready  
- ✔ Core models working correctly  

---

# ✅ Week 2: CRUD for Books & Users

- Created serializers for Books and Users
- Implemented CRUD views (Create, Read, Update, Delete)
- Added API routes
- Tested endpoints using Postman / Thunder Client

*Key Endpoints*
GET /api/books/
POST /api/books/
GET /api/books/<id>/
PUT /api/books/<id>/
DELETE /api/books/<id>/



*Outcome*
- ✔ Fully functional CRUD API  
- ✔ Books and users manageable via API  

---

# ✅ Week 3: Checkout & Return Logic

- Created checkout and return serializers
- Implemented business logic:
  - Only available books can be checked out
  - Book becomes unavailable after checkout
  - Book becomes available again after return
- Added endpoints:
POST /api/checkout/
POST /api/return/



*Outcome*
- ✔ Core library operations working  
- ✔ Real-world validation logic implemented  

---

# ✅ Week 4: Polishing & Authentication

*What was done*
- Added JWT Authentication
- Protected sensitive endpoints
- Implemented pagination
- Improved error handling and API responses
- Added filtering (search books by title)

*Authentication Endpoints*
POST /api/token/
POST /api/token/refresh/


*Outcome*
- ✔ Secure API  
- ✔ Cleaner responses and better UX for API consumers  

---

# ✅ Week 5: Deployment & Documentation

*What was done*
- Installed and configured Gunicorn
- Set up static files collection
- Created `requirements.txt`
- Configured production settings
- Deployed API to PythonAnywhere
- Wrote project documentation

*Root API Response*
```json
{
  "message": "Library Management System API is running",
  "available_endpoints": {
    "admin": "/admin/",
    "books": "/api/books/",
    "token": "/api/token/",
    "token_refresh": "/api/token/refresh/"
  }
}

*Outcome*
✔ API deployed

✔ Production-ready setup

✔ Clear documentation


