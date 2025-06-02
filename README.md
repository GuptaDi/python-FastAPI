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
pip install fastapi uvicorn
```

---

## ▶️ Running the App

Start the development server with:

```bash
uvicorn main:api --reload
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

---

## 🙌 Acknowledgments

Thanks to the [FastAPI](https://fastapi.tiangolo.com/) community for an excellent framework!
