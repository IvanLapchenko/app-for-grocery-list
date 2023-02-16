import sqlite3

groceries = [
    "apples",
    "butter",
    "bread",
    "eggs",
    "tuna",
    "garlic",
    "cheese",
    "milk",
    "juice"
]

groceries = sorted(groceries)

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
    cursor.execute("insert into groceries (name) values (?)", [groceries[i]])
    print("added ", groceries[i])

connection.commit()
connection.close()
