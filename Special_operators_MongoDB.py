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
# 1. $set - Изменяет поле.
users.update_one(
    {"name": "Alina"},
    {"$set": {"age": 21}}
)
# ВАЖНО Без $set документ заменится полностью. Bсе остальные поля удалятся.
print("operator $set")
for user in users.find():
    print(user)
print("************************************")

# 2. $inc - Увеличивает число.
users.update_one(
    {"name": "Alina"},
    {"$inc": {"age": 1}}
)
print("operator $inc")
for user in users.find():
    print(user)
print("************************************")


# 3. $unset - Удаляет поле.
users.update_one(
    {"name": "Alina"},
    {"$unset": {"age": ""}}
)
print("operator $unset")
for user in users.find():
    print(user)
print("************************************")

# 4. $push - Добавляет элемент в массив.
users.update_one(
    {"name": "Tom"},
    {"$push": {"skills": "Flask"}}
)
print("operator $push")
for user in users.find():
    print(user)
print("************************************")

# 5. $pull - Удаляет элемент из массива.
users.update_one(
    {"name": "Tom"},
    {"$pull": {"skills": "Flask"}}
)
print("operator $pull")
for user in users.find():
    print(user)
print("************************************")

# 6. $addToSet - Добавляет в массив только если элемента нет. Без дубликатов
users.update_one(
    {"name": "Tom"},
    {"$addToSet": {"skills": "Python"}}
)
print("operator $addToSet")
for user in users.find():
    print(user)
print("************************************")

# 7. $rename - Переименовывает поле.
users.update_one(
    {"name": "Tom"},
    {"$rename": {"name": "username"}}
)
print("operator $rename")
for user in users.find():
    print(user)
print("************************************")

# 8. Несколько операторов сразу
users.update_one(
    {"name": "Alina"},
    {
        "$set": {"city": "London"},
        "$inc": {"age": 1}
    }
)
print("Combining operators")
for user in users.find():
    print(user)
print("************************************")

# 9. Операторы поиска
# $gt — больше
print("operator $gt")

for user in users.find({"age": {"$gt": 18}}):
    print(user)
print("************************************")

# $lt — меньше
print("operator $lt")

for user in users.find({"age": {"$lt": 30}}):
    print(user)
print("************************************")

# $gte — больше либо равно
print("operator $gte")

for user in users.find({"age": {"$gte": 18}}):
    print(user)
print("************************************")

# $lte — меньше либо равно
print("operator $lte")

for user in users.find({"age": {"$lte": 40}}):
    print(user)
print("************************************")

# $ne — Не равно.
print("operator $ne")

for user in users.find({"name": {"$ne": "Henry"}}):
    print(user)
print("************************************")

# 10. $in - Проверка наличия в списке.

print("operator $in")
for user in users.find({
    "name": {
        "$in": ["Mark", "Alice"]
    }
}):
    print(user)
print("************************************")

# 11. $and - И.
print("operator $and")
for user in users.find({
    "$and": [
        {"age": {"$gt": 18}},
        {"city": "London"}
    ]
}):
    print(user)
print("************************************")

