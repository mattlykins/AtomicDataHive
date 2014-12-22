from classes.species import *
from classes.stout import *
from classes.helpers import *

import os,re
            
            



O2 = species(8,2)
#stoutData = importStout()
readStout(O2,"")
print(O2.levels[1].energy)

print(O2.transitions['1:2'].collision.temperature)

#print(stoutData["fe_2"].transitions['1:2'].CS)
