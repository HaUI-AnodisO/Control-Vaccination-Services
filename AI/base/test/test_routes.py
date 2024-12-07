import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_content():
    with open("test/test_image.jpg", "rb") as image_file:
        response = client.post("/generate-content", files={"image": image_file})
    
    assert response.status_code == 200
    assert "raw_text" in response.json()
    assert "markdown" in response.json()
    assert "json_data" in response.json()
