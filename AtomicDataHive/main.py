from classes.element import *
from classes.species import *
from classes.energylevel import EnergyLevel
from classes.transition import Transition
from classes.helpers import * #@UnusedWildImport

levels=[]
SET_DEBUG={
           'prelevel':False,
           'postLevel':False,
           'preTP':False,
           'postTP':False,
           'preColl':False,
           'postColl':False
           }


with open('o_2.nrg','r') as nrgFile:
    tString=nrgFile.readline()
    for line in nrgFile:
        tList=line.split()
        if "****" in tList[0]:break
        
        tLevel=EnergyLevel()
        
        if SET_DEBUG['prelevel']:print(tList)
        
        tLevel.index=pullValue(tList,'INT')
        tLevel.energy=pullValue(tList,'FLOAT')
        tLevel.g=pullValue(tList, 'FLOAT')
        tLevel.config=pullValue(tList)
        tLevel.term=pullValue(tList)               
        
        levels.append(tLevel)
        
        #Make sure levels are in order
        if int(tLevel.index) != len(levels):sys.exit("Energy Levels out of order")
    
    if SET_DEBUG['postLevel']:    
        for level in levels:
            print(level.index,level.energy,level.g)
        

transitions={}      
with open('o_2.tp','r') as tpFile:
    tString=tpFile.readline()    
    for line in tpFile:
        tList=line.split()
        if "****" in tList[0]:break        
          
        isEina = False
        
        tbEina = pullValue(tList)        
        if tbEina == 'A':isEina=True
        
        tLo = pullValue(tList, 'INT')
        tHi = pullValue(tList, 'INT')
        tTP = pullValue(tList,'FLOAT')
                
        #print(tList)
        
        if len(tList)>0:
            tType = pullValue(tList)
        else:
            tType = None
         
        sKey = str(tLo) + ':' + str(tHi)
        
        if sKey in transitions:
            if isEina:
                transitions[sKey].eina.setTP(tTP, tType)
        else:        
            tTran = Transition(levels[tLo-1],levels[tHi-1])
            if isEina:
                tTran.eina.setTP(tTP, tType)
                transitions[sKey]=tTran

with open('o_2.coll','r') as collFile:
    tString=collFile.readline()     
    tTemps=collFile.readline().split()
    if pullValue(tTemps) != 'TEMP': sys.exit("Coll files should start with TEMP")
     
    for line in collFile:
        tList=line.split()
        if "****" in tList[0]:break
        if 'TEMP' in tList[0]:
            sys.exit("Multiple temperature lines!!!")
        #print(tList)
         
        # Only supporting CS Electron at the moment        
        tx = pullValue(tList)
        if tx != 'CS': sys.exit("NOT CS") 
        tx = pullValue(tList)        
        if tx != 'ELECTRON': sys.exit("NOT ELECTRON")  
         
        #print(tList) 
         
        tLo = pullValue(tList, 'INT')         
        tHi = pullValue(tList, 'INT') 
         
        #print(tList)
         
        sKey = str(tLo) + ":" + str(tHi)

        transitions[sKey].setCS(tTemps,tList)         


#transitions['1:4'].print()
x = element("Carbon","C")
#y = element("Hydrogen","H")

x.atomicnumber=6
y = element("Hydrogen","H")
y.atomicnumber=1

print(x.name,y.name)

a = EnergyLevel(1,6.5,3)
print(a.index)

b = species()
b.name="Hydrogen"
print(b.name)




#transitions['1:2'].print()

