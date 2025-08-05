from enum import IntEnum
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
api = FastAPI()


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length =3, max_length =512, description = "Name of the todo")
    todo_description: str = Field(..., description = "Description of the todo")
    priority: Priority = Field(default=Priority.LOW, description = "Priority of the todo")

class TodoCreate(TodoBase):
    pass

class Todo (TodoBase):
    todo_id: int = Field(...,description="Unique ID of the todo")

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length =3, max_length =512, description = "Name of the todo")
    todo_description: Optional[str] = Field(None, description = "Description of the todo")
    priority: Optional[Priority] = Field(None, description = "Priority of the todo")


all_todos = [
    Todo(todo_id=1, todo_name =  "Gym", todo_description = "Hit the gym", priority = Priority.HIGH),
    Todo(todo_id=2, todo_name =  "Work", todo_description = "Complete your work", priority = Priority.MEDIUM),
    Todo(todo_id=3, todo_name =  "Travel", todo_description = "Travel the world", priority = Priority.MEDIUM),
    Todo(todo_id=4, todo_name =  "Code", todo_description = "Code and build something", priority = Priority.LOW),
    Todo(todo_id=5, todo_name =  "Eat", todo_description = "Enjoy your meals", priority = Priority.HIGH)
]


@api.get('/todos/{id}', response_model=Todo)
def get_todo(id: int):
    for todo in all_todos:
        if todo.todo_id == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@api.get('/todos', response_model = List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@api.post('/todos', response_model = Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1
    new_todo = Todo(todo_id=new_todo_id, todo_name=todo.todo_name, todo_description=todo.todo_description, priority=todo.priority)
    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{id}', response_model=Todo)
def update_todo(id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
    
@api.delete('/todos/{id}', response_model = Todo)
def delete_todo(id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail="Todo not found")
