from classes.element import *
from classes.species import *
from classes.stout import stout


stout().readStout()

for l in stout.levels:
    print(l.index,l.energy,l.g,l.config,l.term)

for x in stout.transitions.items():
    print(x[1].print())      


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

