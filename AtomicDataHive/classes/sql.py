import sqlite3

con = sqlite3.connect('stout.db')

def createDB():
    
    c = con.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS levels
        (id INTEGER PRIMARY KEY,
        energy REAL NOT NULL,
        g REAL NOT NULL)''')
    
    c. execute('''CREATE TABLE IF NOT EXISTS transitions
        (id TEXT PRIMARY KEY,
        lo INTEGER NOT NULL,
        hi INTEGER NOT NULL,
        FOREIGN KEY(lo) REFERENCES levels(id),
        FOREIGN KEY(hi) REFERENCES levels(id))''')
    return c

def dbCommit():
    con.commit()