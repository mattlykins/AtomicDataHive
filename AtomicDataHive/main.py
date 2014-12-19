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
        tLevel.config=pullValue(tList, 'STRING')
        tLevel.term=pullValue(tList, 'STRING')               
        
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
        
        tbEina = pullValue(tList, 'STRING')        
        if tbEina == 'A':isEina=True
        
        tLo = pullValue(tList, 'INT')
        tHi = pullValue(tList, 'INT')
        tTP = pullValue(tList,'FLOAT')
                
        #print(tList)
        
        if len(tList)>0:
            tType = pullValue(tList, 'STRING')
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

# with open('o_2.coll','r') as collFile:
#     tString=collFile.readline()    
#     tTemps=collFile.readline().split()
#     
#     #print(tTemps)
#     tTemps.pop(0)
#     #print(tTemps)
#     
#     for line in collFile:
#         tList=line.split()
#         if "****" in tList[0]:break
#         #print(tList)
#         
#         if tList.pop(0) != 'CS': sys.exit("NOT CS")
#         
#         if tList.pop(0) != 'ELECTRON': sys.exit("NOT ELECTRON")  
#         
#         #print(tList) 
#         
#         tLo = tList.pop(0)
#         is_int(tLo)
#         
#         tHi = tList.pop(0)
#         is_int(tHi)
#         
#         #print(tList)
#         
#         sKey = str(tLo) + ":" + str(tHi)
#         
#         x = transitions[sKey].setCS(tTemps,tList)
#         
#         
# 
# transitions['1:5'].print()



