# Fast API

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
It came to solve the drawbacks of Flask(another old framework).

To get started with FastAPI, you need to install FastAPI and Uvicorn using pip. Uvicorn is an Asynchronous Server Gateway Interface (ASGI) server used for production.

FastAPI has the advantage of handling requests asynchronously. All you need to do is to put the async keyword before a function when declaring endpoints. For example, async def my_endpoint():

### Is FastAPI built on Flask?

Flask, which is a Python micro framework, is used for building FastAPI. It is a Python library that offers an easy way to create web applications with the help of HTML/CSS or Python. Unlike Flask, FastAPI doesn’t have a built-in development server, so an ASGI server similar to Daphne or Uvicorn is used when required. FastAPI’s speed is largely because ASGI is the server in which it was built and it supports asynchronous code.

#### WSGI and ASGI

WSGI is a Python standard specifically written for web applications and servers to interface with each other. It was introduced in 1999. Novice programmers can sometimes find it challenging to start with Python. However, those who have worked with PHP or Ruby will have an easier time understanding it.

ASGI was introduced by the inventors of FastAPI. It is a specification to build event-driven, asynchronous web applications. It comes with an API framework which means you can use any framework to build an application.

FastAPI and ASGI are complementary in the following ways:

They allow you to have tools and libraries that make them easy to use.
They allow you to write any code that is event-driven and asynchronous.

# 📝 FastAPI To-Do List API

A simple, lightweight To-Do List API built with **FastAPI** and **Pydantic**. It supports basic task management operations including fetching, creating, and updating tasks with prioritization.

---

## 🚀 Features

- 📥 Create new to-do items
- 📋 Fetch individual or all tasks
- ✏️ Update existing tasks
- ⚙️ Priority handling with enums (HIGH, MEDIUM, LOW)
- 📦 JSON-based API responses

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **FastAPI** for the web framework
- **Pydantic** for data validation
- **Uvicorn** (recommended) as the ASGI server

---

## 📂 Project Structure

```bash
.
├── main.py          # Main application code
├── README.md        # Project documentation
```

---

## 📌 Requirements

Install dependencies using:

```bash
pip install "fastapi[standard]"
```

---

## ▶️ Running the App

Start the development server with:

```bash
fastapi dev simpleHelloWorld.py
```

Visit the interactive API docs at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 API Endpoints

### `GET /todos/{todo_id}`

Fetch a specific to-do item by ID.

### `GET /todos?first_n=N`

Fetch the first `N` to-do items.

### `POST /todos`

Create a new to-do.

### `PUT /todos/{todo_id}`

Update an existing to-do.

---

## 📌 Example To-Do JSON

```json
{
  "todo_name": "Finish report",
  "todo_description": "Write the quarterly financial report",
  "priority": 1
}
```

---

## ✅ Future Enhancements

- Add persistence with a database (e.g., SQLite, PostgreSQL)
- Add delete endpoint
- Add user authentication
- Include due dates and tags

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

##### NOTE:

async functions can be used when you are dealing with the DB.
In fastAPI, you can mix these 2 approaches - synchronous and async functions.
Automatic interactive AI docs are generated with the Swagger UI - localhost:9999/docs
