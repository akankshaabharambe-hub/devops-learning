from app.main import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_tools_endpoint_has_kubernetes():
    client = app.test_client()
    response = client.get("/tools")
    data = response.get_json()
    assert "kubernetes" in data
    assert "containers" in data["kubernetes"]
