from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to gym'},
    {'todo_id': 2, 'todo_name': 'Study', 'todo_description': 'Prepare for exam'},
    {'todo_id': 3, 'todo_name': 'Groceries Shopping', 'todo_description': 'Buy Milk'},
    {'todo_id': 4, 'todo_name': 'Meditate', 'todo_description': 'Meditate 20 mins'},

]


# localhost:9999/todos/2
@api.get("/todos/{todo_id}")
def get_todo(todo_id):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}


# localhost:9999/todos -- With query parameters
@api.get("/todos")
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos


@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }

    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{todo_id}')
def edit_todo(todo_id: int,  newtodo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = newtodo['todo_name']
            todo['todo_description'] = newtodo['todo_description']
            return todo
    return "Error, todo not found"


@api.delete('/todos/{todo_id}')
def remove_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    return "Error, todo not found"
