from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

client.admin.command("ping")
print("Connected!")

# ******************************************************
# Создание БД
db = client["usersdatabase"]

# ******************************************************
# Создание коллекции
users = db["users"]

# ******************************************************
# Добавление документа
"""
users.insert_many([
    {"name": "Alina", "age": 28},
    {"name": "Holly", "age": 42},
    {"name": "Elly", "age": 27},
    {"name": "Henry", "age": 33},
    {"name": "Tom", "age": 28}
])
"""

# ******************************************************
# ПОЛУЧЕНИЕ ДАННЫХ

# Один документ
print(users.find_one())

# Все документы
for user in users.find():
    print(user)

# Special operators MongoDB


