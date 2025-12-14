Library Management System – Week 1 Progress

Week 1 Focus: Project Setup & Basic Models

✅ 1. Project Setup

During Week 1, the main goal was to set up the foundation of the Library Management System.
The following tasks were completed:

✔️ Created Django Project and App

Initialized a new Django project.

Created the main application for the system.

✔️ Set Up Virtual Environment

Created and activated a virtual environment.

Installed all necessary project dependencies inside the environment.

✔️ Installed Django REST Framework (DRF)

Added djangorestframework to the project.

Updated settings.py to include "rest_framework" in INSTALLED_APPS.

🧱 2. Basic Models Implemented

Three core models were created to structure the system:

📌 User Model

Stores basic user information.

Represents people who borrow books.

📌 Book Model

Contains details about each book in the library.

Fields include: title, author, category, availability status.

📌 Checkout Model

Tracks which user borrowed which book and when.

Helps manage returns and borrowing history.

🗄️ 3. Database Configuration
✔️ Ran Migrations

Created migration files for all models.

Successfully applied migrations to generate database tables.

✔️ Tested Models in Django Shell

Loaded Django shell using python manage.py shell.

Created sample User, Book, and Checkout objects.

Verified relationships and data saving correctly.
