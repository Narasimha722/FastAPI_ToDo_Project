from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from todo_models import Task
from database import create_db_and_tables, get_session

app = FastAPI()
templates = Jinja2Templates(directory="templates")

create_db_and_tables()

@app.get("/")
def read_root(request: Request):
    session = get_session()
    tasks = session.query(Task).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/")
def create_task(task_id: int = Form(...), title: str = Form(...)):
    session = get_session()
    if session.get(Task, task_id):
        return RedirectResponse("/", status_code=303)  # prevent duplicate IDs
    task = Task(id=task_id, title=title)
    session.add(task)
    session.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/complete/{task_id}")
def complete_task(task_id: int):
    session = get_session()
    task = session.get(Task, task_id)
    if task:
        task.completed = True
        session.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/delete/{task_id}")
def delete_task(task_id: int):
    session = get_session()
    task = session.get(Task, task_id)
    if task:
        session.delete(task)
        session.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/edit/{task_id}")
def edit_task(request: Request, task_id: int):
    session = get_session()
    task = session.get(Task, task_id)
    if not task:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("edit.html", {"request": request, "task": task})

@app.post("/update/{task_id}")
def update_task(task_id: int, title: str = Form(...), completed: bool = Form(False)):
    session = get_session()
    task = session.get(Task, task_id)
    if task:
        task.title = title
        task.completed = completed
        session.commit()
    return RedirectResponse("/", status_code=303)
