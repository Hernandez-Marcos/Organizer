# Organizer – Django Task Manager

Organizer is a simple task management web application built with Django.

This project was created as a **learning project**, focused on backend development and understanding how Django works internally, rather than on advanced frontend design or features.

---

## What this project includes

- Real user authentication:
  - Register
  - Login
  - Logout
- Custom user model
- User-based data protection (each user can only see and manage their own tasks)
- Full CRUD functionality for tasks:
  - Create tasks
  - View task list
  - Update tasks
  - Delete tasks
- Delete confirmation page
- Authentication-required views
- Flash messages (Django messages framework)
- Clean and simple URL structure
- Correct redirects after actions (login, logout, create, update, delete)
- Base template with block inheritance
- CSRF protection
- Separation of concerns:
  - Apps
  - URLs
  - Views
  - Templates

---

## Tech Stack

- Python
- Django
- HTML (Django templates)
- SQLite (default Django database)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/organizer.git
cd organizer
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies using the requirements file:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## Project Status

This is a **functional initial version**.

---

## Purpose of the project

This project was built purely for **learning purposes**.

The main goals were to practice and understand:

- Django authentication flow
- Custom user models
- Protecting user data
- CRUD patterns
- URL routing
- Template inheritance
- Backend logic organization

---

## Author

Marcos  
Learning Django and backend web development

