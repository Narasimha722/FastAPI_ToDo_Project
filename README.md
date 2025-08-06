# 📝 FastAPI To-Do List App

A simple and clean web-based To-Do List application built with **FastAPI**, **SQLModel**, **Jinja2 Templates**, and **SQLite**.

## 🚀 Features

- ✅ Add tasks with custom `task_id` and title
- ✏️ Edit task title and completion status
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 📄 Clean Bootstrap-powered HTML UI
- 🗂 Persistent data using SQLite
- 🌐 Fully backend-rendered Web UI using FastAPI + Jinja2

🧠 Why FastAPI?
-----------------------------------------------------------
We chose FastAPI because it's:

⚡ Blazingly fast — built on top of Starlette & Pydantic

⛳ Easy to use — simple decorators, auto request validation

📦 Built-in async support — scales well for modern web backends

📄 Automatic interactive API docs — powered by Swagger UI

🔒 Modern standards — follows OpenAPI, JSON Schema, OAuth2

FastAPI is perfect for projects where performance, developer productivity, and clean code matter.

🔍 API Docs with Swagger UI
FastAPI provides auto-generated, interactive Swagger UI to test your API endpoints. It’s available at:

http://127.0.0.1:8000/docs

You also get ReDoc (alternative view):

http://127.0.0.1:8000/redoc

With Swagger, you can:
-----------------------------------------------------------
✅Try out endpoints directly in your browser

✅See available routes, input/output schemas

✅Debug API without writing a single line of frontend

✅This makes API testing fast and visual — no need for Postman or CURL.

assets\Swagger.png

---

## 📁 Project Structure

```bash
fastapi_todo_app/
├── main.py # Main FastAPI app
├── database.py # DB setup and session config
├── schemas.py # Task model using SQLModel
├── requirements.txt # Project dependencies
└── templates/ # HTML templates (Jinja2)
├── index.html # Home page for listing/adding tasks
└── edit.html # Edit task form
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Narasimha722/FastAPI_ToDo_Project.git
cd FastAPI_ToDo_Project
```

2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

▶️ Running the App

```bash
uvicorn main:app --reload
```

Visit the app in your browser at:
👉 http://127.0.0.1:8000

assets\FastAPI_Todo_Home page.png

🧪 Features Overview
------------------------------
Add task with ID + title

Edit task with check/uncheck "completed"

Click to mark task as done

Delete individual task

All data saved in database.db

📦 Requirements
-------------------------
Python 3.8+

FastAPI

SQLModel

Jinja2

Uvicorn

python-multipart

📚 Learnings
---------------------------------------------------
How to use FastAPI for full-stack web development

Using Jinja2 templates for dynamic web UI

Handling form submissions in FastAPI

Building REST endpoints

SQLite database interaction via SQLModel
