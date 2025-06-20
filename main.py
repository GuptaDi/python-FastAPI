"""
This module is an advanced version of todoApp file.
With proper typings, and a better documentation feature.
"""
from enum import IntEnum
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

api = FastAPI()


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


# define the parent class
class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512,
                           description='Name of the todo')
    todo_description: str = Field(..., description='Description of the todo')
    priority: Priority = Field(
        default=Priority.LOW, description='Priority of the todo')


# it will just inherit the base class. While creation I want to add all these fields.
class TodoCreate(TodoBase):
    pass


# This class we created as our response model. So, it will have all the fields.
class Todo(TodoBase):
    todo_id: int = Field(..., description='Unique identifier of the todo')


# During update, I dont have to update all the fields at the same time. So, I am adding optional.
class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(
        None, min_length=3, max_length=512, description='Name of the todo')
    todo_description: Optional[str] = Field(
        None, description='Description of the todo')
    priority: Optional[Priority] = Field(
        None, description='Priority of the todo')


all_todos = [
    Todo(todo_id=1, todo_name='Sports',
         todo_description='Go to the gym', priority=Priority.HIGH),
    Todo(todo_id=2, todo_name='Study',
         todo_description='Prepare for exam', priority=Priority.LOW),
    Todo(todo_id=3, todo_name='Groceries Shopping',
         todo_description='Buy Milk', priority=Priority.MEDIUM),
    Todo(todo_id=4, todo_name='Meditate',
         todo_description='Meditate 20 mins', priority=Priority.HIGH),
]


# Using a path parameter.
# localhost:9999/todos/2
@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail='Todo not found for fetch')


# Using a query parameter.
# localhost:9999/todos?first_n=3
@api.get("/todos", response_model=List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos


# Create a new Todo
@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1
    new_todo = Todo(todo_id=new_todo_id, todo_name=todo.todo_name,
                    todo_description=todo.todo_description, priority=todo.priority)

    all_todos.append(new_todo)

    return new_todo


# Edit an existing todo
@api.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_name is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.todo_name is not None:
                todo.priority = updated_todo.priority
            return todo

    raise HTTPException(status_code=404, detail='Todo not found for update')


# Remove todo
@api.delete("/todos/{todo_id}")
def remove_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo

    raise HTTPException(status_code=404, detail='Todo not found for delete')
