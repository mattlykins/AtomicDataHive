from classes.species import *
from classes.stout import *
from classes.helpers import *
from classes.sql import *

import os,re
            
            



O2 = species(8,2)
Fe2 = species(26,2)


#stoutData = importStout()
#readStout(Fe2,"")
readStout(O2,"")

con = dbConnect('stout.db')
c = dbCreate(con)

dbAddSpecies(c,'O_2',8,2)

c.execute("SELECT * from species")
print(c.fetchall())

#print(Fe2.transitions['1:2'].collision.collData)
#print(O2.transitions['1:5'].collision.collData)
#print(O2.levels[1].energy)

#print(O2.transitions['1:2'].collision.temperatur

#stout.print(stoutData)



for level in O2.levels:    
    #c.execute("INSERT INTO levels(id,energy,g,speciesid) VALUES (?,?,?,?)",(level.index,level.energy,level.g,0))
    dbAddLevel(c,int(level.index),float(level.energy),float(level.g),int(1))
 
for key,value in O2.transitions.items():
    dbAddTransition(c,key,value.lo.index,value.hi.index,int(1))
      
dbCommit(con)

c.execute("SELECT * FROM transitions NATURAL JOIN species")
print(c.fetchone())
    
# c.execute("SELECT * FROM transitions T LEFT JOIN levels L ON T.lo=L.id LEFT JOIN levels L2 ON T.hi=L2.id")
# test=c.fetchall()
# for za in test:
#     print(za)

