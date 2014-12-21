from classes.species import *
from classes.stout import *
from classes.helpers import *

import os,re

# Program Start Here
# Take in parameters: DB Type (Stout) and import location (file or folder)

isStout = True
location = ".\\stout\\"



# Generate list of paths
# For stout, the 3 files will be in the same directory
pathList = []
for root, dirs, files in os.walk(location):
    for file in files:
        if file.endswith(".nrg"):
            pathList.append(os.path.join(root,file))
            
            
#Process pathList into element and species


for path in pathList:
    filePath = path.split('\\')
    fileName = filePath[-1]
    nameList = re.split('[_,.]',fileName)
    
    elemName = pullValue(nameList)
    specIon = pullValue(nameList, 'INT')
    elemIon = specIon - 1
    
    #print(elemName,specIon)
    
    #-------------------------------------------



O2 = species(8,2)
print(O2.spectrumName)
readStout(O2)

for x in O2.transitions.items():
    x[1].print()




    


#run stout
#stout(pathList)

# for l in stout.levels:
#     print(l.index,l.energy,l.g,l.config,l.term)
#  
# for x in stout.transitions.items():
#     print(x[1].print())      


# #transitions['1:4'].print()
# x = element("Carbon","C")
# #y = element("Hydrogen","H")
# 
# x.atomicnumber=6
# y = element("Hydrogen","H")
# y.atomicnumber=1
# 
# print(x.name,y.name)
# 
# a = EnergyLevel(1,6.5,3)
# print(a.index)
# 
# b = species()
# b.name="Hydrogen"
# print(b.name)




#transitions['1:2'].print()

