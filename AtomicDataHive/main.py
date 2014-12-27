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
#print(Fe2.transitions['1:2'].collision.collData)
#print(O2.transitions['1:5'].collision.collData)
#print(O2.levels[1].energy)

#print(O2.transitions['1:2'].collision.temperatur

#stout.print(stoutData)



for level in O2.levels:    
    #c.execute("INSERT INTO levels(id,energy,g,speciesid) VALUES (?,?,?,?)",(level.index,level.energy,level.g,0))
    dbAddLevel(c,int(level.index),float(level.energy),float(level.g),int(1))
 
for key,value in O2.transitions.items():
    c.execute("INSERT INTO transitions(name,lo,hi) VALUES (?,?,?)",(key,value.lo.index,value.hi.index))
      
dbCommit(con)
lower = 2
higher = 3
id = str(lower) + ":" + str(higher),
c.execute('SELECT * FROM transitions')

x = c.fetchall()

for i in x:
    print(i)

