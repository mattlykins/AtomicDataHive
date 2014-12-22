from classes.species import *
from classes.stout import *
from classes.helpers import *

import os,re
            
            



O2 = species(8,2)
stoutData = importStout()

print(stoutData["fe_2"].transitions['1:2'].CS)
