import requests

# Define the base URL for your FastAPI app
BASE_URL = "http://127.0.0.1:8000"

# Test GET request
def test_get_item():
    response = requests.get(f"{BASE_URL}/items/1")
    print("GET /items/1:", response.json())
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

# Test GET request with query parameters
def test_get_item_with_query():
    response = requests.get(f"{BASE_URL}/items/1?q=fastapi")
    print("GET /items/1?q=fastapi:", response.json())
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "fastapi"}

# Test GET request with non-existent item
def test_get_item_not_found():
    response = requests.get(f"{BASE_URL}/items/0")
    print("GET /items/0:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

# Test POST request
def test_create_item():
    payload = {"name": "Apple", "price": 0.5}
    response = requests.post(f"{BASE_URL}/items/", json=payload)
    print("POST /items/:", response.json())
    assert response.status_code == 200
    assert response.json() == {"item_name": "Apple", "item_price": 0.5}

if __name__ == "__main__":
    test_get_item()
    test_get_item_with_query()
    test_get_item_not_found()
    test_create_item()
