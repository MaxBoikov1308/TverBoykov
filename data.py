import sqlite3
import db

def Save(name, start, score, t1, t2, t3, n):
    if sqlite3.connect("dat.sqlite"):
        con = sqlite3.connect("dat.sqlite")
    else:
        db.DB()
        con = sqlite3.connect("dat.sqlite")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса
    cur.execute("""INSERT INTO saves(Name, Start, Score, Tower1, Tower2, Tower3, N)
                VALUES(?, ?, ?, ?, ?, ?, ?)""", (name, start, score, t1, t2, t3, n))
    con.commit()

    con.close()

def Load(n):
    if sqlite3.connect("dat.sqlite"):
        con = sqlite3.connect("dat.sqlite")
    else:
        db.DB()
        con = sqlite3.connect("dat.sqlite")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса
    result = cur.execute("""SELECT * FROM saves
WHERE Name = ?""", (n,)).fetchall()
    return list(result[0])[3:]
