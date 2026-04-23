from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to CI/CD Pipeline Demo" in response.data

def test_deploy():
    client = app.test_client()
    response = client.get("/deploy")
    assert response.status_code == 200
    assert b"deployment successful" in response.data