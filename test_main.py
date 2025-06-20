from fastapi.testclient import TestClient
from main import api, all_todos


test_client = TestClient(api)


# Before each step, we will delete all the todos. SO, 1 step doesn't touch another.
# def setup_function():
#    all_todos.clear()


def test_get_todos():
    response = test_client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_get_todo_by_id_success():
    response = test_client.get("/todos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["todo_id"] == 1


def test_get_todo_by_id_not_found():
    response = test_client.get("/todos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found for fetch"


def test_create_todo():
    payload = {"todo_name": "Test Todo",
               "todo_description": "test_todo_description", "priority": 3}
    response = test_client.post("/todos", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["todo_name"] == "Test Todo"
    assert "todo_id" in data


def test_update_todo():
    payload = {
        "todo_name": "Updated Name"
    }
    response = test_client.put("/todos/1", json=payload)
    assert response.status_code == 200
    assert response.json()["todo_name"] == "Updated Name"


def test_delete_todo():
    response = test_client.delete("/todos/2")
    assert response.status_code == 200
    assert response.json()["todo_id"] == 2
