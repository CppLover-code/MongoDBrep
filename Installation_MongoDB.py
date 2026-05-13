"""
1. Скачиваем и устанавливаем:
MongoDB Community Server
MongoDB Compass - графический интерфейс для MongoDB.
2. Установка библиотеки pymongo
pip install pymongo
"""
# Первое подключение
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Создание БД
db = client["mydatabase"]

# Создание коллекции
users = db["users"]

# Добавление документа
user = {
    "name": "Mark",
    "age": 25
}

users.insert_one(user)

# ПОЛУЧЕНИЕ ДАННЫХ

# Один документ
print(users.find_one())

# Все документы
for user in users.find():
    print(user)
