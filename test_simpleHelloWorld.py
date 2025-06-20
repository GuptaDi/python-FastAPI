from fastapi.testclient import TestClient
from simpleHelloWorld import app

test_client = TestClient(app)


def test_index():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
