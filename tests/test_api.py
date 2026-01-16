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

def test_rate_bar(client):
    r = client.post("/api/bars", json={"name": "Rated Bar", "city": "Granada"})
    bar_id = r.json()["id"]

    r = client.post(f"/api/bars/{bar_id}/rating", json={"rating": 5})
    assert r.status_code == 200
    assert r.json()["avg_rating"] == 5.0
