import sqlite3

def dbConnect(fileName):
    con = sqlite3.connect(fileName)
    return con

def dbCreate(con):
    
    c = con.cursor()
    
    c.execute('''DROP TABLE IF EXISTS levels''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS levels
        (id INTEGER PRIMARY KEY,
        energy REAL NOT NULL,
        g REAL NOT NULL,
        speciesid INTEGER NOT NULL,
        FOREIGN KEY(speciesid) REFERENCES species(id))''')
    
    c.execute('''DROP TABLE IF EXISTS transitions''')
    
    c. execute('''CREATE TABLE IF NOT EXISTS transitions
        (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        lo INTEGER NOT NULL,
        hi INTEGER NOT NULL,
        FOREIGN KEY(lo) REFERENCES levels(id),
        FOREIGN KEY(hi) REFERENCES levels(id))''')
    
    c.execute('''DROP TABLE IF EXISTS species''')
    c.execute('''CREATE TABLE IF NOT EXISTS species
        (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        z INTEGER NOT NULL,
        ion INTEGER NOT NULL)''')
    return c


def dbCommit(con):
    con.commit()
    
def dbAddSpecies(c,name,z,ion):
    c.execute("INSERT INTO species(name,z,ion) VALUES (?,?,?)",(name,z,ion,))
    SET_DEBUG_DB = True
    if(SET_DEBUG_DB):
        print("Inserted %s, Z = %i, ION = %i into db" % (name,z,ion,))
        
def dbAddLevel(c,index,energy,g,speciesid):
    c.execute("INSERT INTO levels(id,energy,g,speciesid) VALUES (?,?,?,?)",(index,energy,g,speciesid,))
    SET_DEBUG_DB = True
    if(SET_DEBUG_DB):
        c.execute("SELECT name FROM species WHERE species.id=?", (speciesid,))
        tSpec = c.fetchone()
        print("Inserted %i\t%e\t%.1f: from %s" % (index,energy,g, tSpec[0]))
        