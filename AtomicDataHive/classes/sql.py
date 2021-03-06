import sqlite3

def dbConnect(fileName):
    con = sqlite3.connect(fileName)    
    return con

def dbCreate(con):
    
    c = con.cursor()
    
    c.execute('''DROP TABLE IF EXISTS levels''')
    c.execute('''DROP TABLE IF EXISTS transitions''')
    c.execute('''DROP TABLE IF EXISTS species''')
    c.execute('''DROP TABLE IF EXISTS colliders''')
    c.execute('''DROP TABLE IF EXISTS colltype''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS levels
        (levelid INTEGER PRIMARY KEY,
        dex INTEGER NOT NULL,
        energy REAL NOT NULL,
        g REAL NOT NULL,
        speciesid INTEGER NOT NULL,
        FOREIGN KEY(speciesid) REFERENCES species(speciesid))''')    
    
    
    c. execute('''CREATE TABLE IF NOT EXISTS transitions
        (transitionid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        lo INTEGER NOT NULL,
        hi INTEGER NOT NULL,
        speciesid INTEGER NOT NULL,
        FOREIGN KEY(lo) REFERENCES levels(levelid),
        FOREIGN KEY(hi) REFERENCES levels(levelid),        
        FOREIGN KEY(speciesid) REFERENCES species(speciesid))''')
    
    
    c.execute('''CREATE TABLE IF NOT EXISTS species
        (speciesid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        z INTEGER NOT NULL,
        ion INTEGER NOT NULL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS colliders
        (colliderid INTEGER PRIMARY KEY,
        name TEXT NOT NULL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS colltype
        (colltypeid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        israte INTEGER NOT NULL,
        collider TEXT NOT NULL,
        FOREIGN KEY(collider) REFERENCES colliders(colliderid) )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS transprob
        (transprobid INTEGER PRIMARY KEY,
        e1 REAL NOT NULL,
        e2 REAL NOT NULL,
        e3 REAL NOT NULL,
        m1 REAL NOT NULL,
        m2 REAL NOT NULL,
        m3 REAL NOT NULL,
        transitionid INTEGER NOT NULL,
        speciesid INTEGER NOT NULL,
        FOREIGN KEY(transitionid) REFERENCES transitions(transitionid),
        FOREIGN KEY(speciesid) REFERENCES species(speciesid) )''')
    
    con.execute("PRAGMA foreign_keys = ON")
    return c


def dbCommit(con):
    con.commit()
    
def dbAddSpecies(c,name,z,ion):
    c.execute("INSERT INTO species(name,z,ion) VALUES (?,?,?)",(name,z,ion,))
    SET_DEBUG_DB = False
    if(SET_DEBUG_DB):
        print("Inserted %s, Z = %i, ION = %i into db" % (name,z,ion,))
    rowid = getInsertedRow(c)
    return rowid
        
def dbAddLevel(c,index,energy,g,speciesid):
    c.execute("INSERT INTO levels(dex,energy,g,speciesid) VALUES (?,?,?,?)",(index,energy,g,speciesid,))
    SET_DEBUG_DB = False
    if(SET_DEBUG_DB):
        c.execute("SELECT name FROM species WHERE species.speciesid=?", (speciesid,))
        tSpec = c.fetchone()
        print("Inserted %i\t%e\t%.1f: from %s" % (index,energy,g, tSpec[0]))
    rowid = getInsertedRow(c)
    return rowid
        
def dbAddTransition(c,name,lo, hi,speciesid):
    c.execute("INSERT INTO transitions(name,lo,hi,speciesid) VALUES (?,?,?,?)",(name,lo,hi,speciesid))
    SET_DEBUG_DB = True
    if(SET_DEBUG_DB):
        c.execute("SELECT name FROM species WHERE species.speciesid=?", (speciesid,))
        tSpec = c.fetchone()
        print("Inserted %s\t%i\t%i:from %s" % (name,lo, hi, tSpec[0]))
    rowid = getInsertedRow(c)
    return rowid
        
def dbAddCollider(c,name):
    c.execute("INSERT INTO colliders(name) VALUES (?,)",(name,))
    SET_DEBUG_DB = False
    if(SET_DEBUG_DB):
        print("Added %s to db:%i\t%s" % (name,))
    rowid = getInsertedRow(c)
    return rowid
        
def dbAddCollType(c,name,isRate,collider):
    c.execute("INSERT INTO colltype(name,israte,collider) VALUES (?,?,?,)",(name,isRate,collider))
    SET_DEBUG_DB = False
    if(SET_DEBUG_DB):
        print("Added %s to db:%i\t%s" % (name,isRate,collider,))
    rowid = getInsertedRow(c)
    return rowid
        
def dbAddTransitionProbability(c,e1,e2,e3,m1,m2,m3,transitionid,speciesid):
    c.execute("INSERT INTO transprob(e1,e2,e3,m1,m2,m3,transitionid,speciesid) VALUES (?,?,?,?,?,?,?,?)",(e1,e2,e3,m1,m2,m3,transitionid,speciesid,))
    SET_DEBUG_DB = True
    if SET_DEBUG_DB:
        print("E1 = %e" % e1)
    rowid = getInsertedRow(c)
    return rowid
        
def getInsertedRow(c):
    c.execute("SELECT last_insert_rowid()")
    rowid = c.fetchone()[0]
    return rowid
    
        