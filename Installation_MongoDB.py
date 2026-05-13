"""
1. Скачиваем и устанавливаем:
MongoDB Community Server
MongoDB Compass - графический интерфейс для MongoDB.
2. Установка библиотеки pymongo
pip install pymongo
"""
# ******************************************************
# Первое подключение
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

client.admin.command("ping")
print("Connected!")

# ******************************************************
# Создание БД
db = client["mydatabase"]

# ******************************************************
# Создание коллекции
users = db["users"]

# ******************************************************
# Добавление документа
user = {
    "name": "Mark",
    "age": 25
}

users.insert_one(user)

users.insert_one({
    "name": "Alice",
    "age": 22
})

# ******************************************************
# ПОЛУЧЕНИЕ ДАННЫХ

# Один документ
print(users.find_one())

# Все документы
for user in users.find():
    print(user)

# ******************************************************
# Поиск по условию
for user in users.find({"age": 25}):
    print(user)

# ******************************************************
# Обновление документа

users.update_one(
    {"name": "Mark"},
    {"$set": {"age":26}}
)

# ******************************************************
# Удаление документа

users.delete_one({"name": "Mark"})