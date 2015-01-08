from classes.species import *
from classes.stout import *
from classes.helpers import *
from classes.sql import *

import os,re
            
            



O2 = species(8,2)
Fe2 = species(26,2)


stoutData = importStout()
#readStout(Fe2,"")
#readStout(O2,"")

#dbStout(O2)

# con = dbConnect('stout.db')
# c = dbCreate(con)
# 
# dbAddSpecies(c,'O_2',8,2)
# dbAddSpecies(c, 'fe_2', 26, 2)
# 
# c.execute("SELECT * from species")
# print(c.fetchall())

#print(Fe2.transitions['1:2'].collision.collData)
#print(O2.transitions['1:5'].collision.collData)
#print(O2.levels[1].energy)






