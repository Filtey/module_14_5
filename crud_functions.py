import sqlite3

def initiate_db():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS Users(
       id INTEGER PRIMARY KEY, 
       username TEXT NOT NULL,
       email TEXT NOT NULL,
       age INTEGER NOT NULL,
       balance INTEGER NOT NULL
       )
       ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return products



def add_user(username, email, age):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)", (f"{username}", f"{email}", f"{age}", f"{1000}"))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ?", (f"{username}",))
    rezult = cursor.fetchall()
    connection.commit()
    connection.close()
    if not rezult:
        return False
    else:
        return True
