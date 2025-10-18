from fastapi.testclient import TestClient 
from app.main import app 
client = TestClient(app) 
def test_root(): 
    response = client.get("/") 
assert response.status_code == 200 
assert response.json() == {"message": "Bienvenido a la API de tareas!"} 
def test_create_item(): 
    response = client.post("/items", json={"name": "Tarea 1", "description": 
"Primera tarea"}) 
assert response.status_code == 200 
    data = response.json() 
assert data["id"] == 1 
assert data["name"] == "Tarea 1" 
def test_get_items(): 
    response = client.get("/items") 
assert response.status_code == 200 
    items = response.json() 
assert len(items) > 0 
def test_get_item_by_id(): 
    response = client.get("/items/1") 
assert response.status_code == 200 
    item = response.json() 
assert item["id"] == 1 
def test_update_item(): 
    response = client.put("/items/1", json={"name": "Tarea Actualizada", 
"description": "Nueva descripción"}) 
assert response.status_code == 200 
    item = response.json() 
assert item["name"] == "Tarea Actualizada" 
def test_delete_item(): 
    response = client.delete("/items/1") 
assert response.status_code == 200 
assert response.json() == {"message": "Item eliminado"} 
    response = client.get("/items/1") 
assert response.status_code == 404