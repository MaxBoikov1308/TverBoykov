import sqlite3


class DB:

    conn = sqlite3.connect("dat.sqlite")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE "saves" (
	"id"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT,
	"Start"	TEXT,
	"Score"	INTEGER,
	"Tower1"	TEXT,
	"Tower2"	TEXT,
	"Tower3"	TEXT,
	"N"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
    ''')

    conn.commit()
    conn.close()
