import sqlite


def collection(DATEBASE_URL):
    db=sqlite.connect(DATEBASE_URL)
    c=db.cursor()

def query(c):
    c.query(sql,()).fetchall()
    
