import requests

BASE_URL = "http://127.0.0.1:5000"

# 1. POST /items - Добавление нового товара
def add_item():
    url = f"{BASE_URL}/items"
    data = {
        "name": "Laptop",
        "quantity": 10,
        "price": 1200,
        "category": "Electronics"
    }
    response = requests.post(url, json=data)
    print("Add Item Response:", response.json(), response.status_code)

# 2. GET /items - Получение списка товаров
def get_items():
    url = f"{BASE_URL}/items"
    response = requests.get(url)
    print("Get Items Response:", response.json(), response.status_code)

# 3. GET /items?category=Electronics - Получение товаров по категории
def get_items_by_category():
    url = f"{BASE_URL}/items?category=Electronics"
    response = requests.get(url)
    print("Get Items by Category Response:", response.json(), response.status_code)

# 4. PUT /items/<item_id> - Обновление товара
def update_item(item_id):
    url = f"{BASE_URL}/items/{item_id}"
    data = {
        "name": "Updated Laptop",
        "quantity": 5,
        "price": 1100,
        "category": "Electronics"
    }
    response = requests.put(url, json=data)
    print("Update Item Response:", response.json(), response.status_code)

# # 5. DELETE /items/<item_id> - Удаление товара
# def delete_item(item_id):
#     url = f"{BASE_URL}/items/{item_id}"
#     response = requests.delete(url)
#     print("Delete Item Response:", response.json(), response.status_code)

# 6. GET /reports/summary - Генерация отчета
def generate_report():
    url = f"{BASE_URL}/reports/summary"
    response = requests.get(url)
    print("Generate Report Response:", response.json(), response.status_code)

# 7. GET /reports/summary?format=csv - Генерация CSV отчета
def generate_csv_report():
    url = f"{BASE_URL}/reports/summary?format=csv"
    response = requests.get(url)
    print("Generate CSV Report Response:", response.json(), response.status_code)

# Выполнение всех запросов
if __name__ == "__main__":
    add_item()  # Добавление товара
    get_items()  # Получение всех товаров
    get_items_by_category()  # Получение товаров по категории
    update_item(2)  # Обновление товара с ID 1
    # delete_item(1)  # Удаление товара с ID 1
    generate_report()  # Генерация отчета
    generate_csv_report()  # Генерация CSV отчета