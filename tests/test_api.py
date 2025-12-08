from fastapi.testclient import TestClient
from app.main import app

def test_create_bar_and_list():
    with TestClient(app) as client:
        r = client.post("/api/bars", json={"name": "Bar Uno", "city": "Granada"})
        assert r.status_code == 201

        r2 = client.get("/api/bars")
        assert r2.status_code == 200
        data = r2.json()
        assert len(data["items"]) >= 1
