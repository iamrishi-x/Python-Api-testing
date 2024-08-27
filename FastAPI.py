from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, title: str = None):
    print("\nIn GET \nitem_id", item_id, " | title", title)
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "title": title}

@app.post("/items/")
def create_item(item: dict):
    print(f"\nIn POST \nname - {item['name']} and price - {item['price']}")
    return {"item_name": item["name"], "item_price": item["price"]}


"""
------------ using FastAPI swagger UI ---------------
For fastAPI - http://127.0.0.1:8000/docs
POST - 
{"name": "Widget", "price": 9.99}

------------- Using Postman -------------------

For GET - 
url - http://127.0.0.1:8000/items/7?title=zzz

-----------
For POST - 
url - http://127.0.0.1:8000/items/
body - {"name": "Widget", "price": 9.99}

"""