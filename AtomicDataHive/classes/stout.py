from classes.energylevel import EnergyLevel
from classes.transition import Transition
from classes.helpers import * #@UnusedWildImport
class stout():
    
    def __init__(self,spec):
        self.species = spec
        readstout(self,spec)
        
    def readStout(self,spec):        
        
        SET_DEBUG={
           'prelevel':False,
           'postLevel':False,
           'preTP':False,
           'postTP':False,
           'preColl':False,
           'postColl':False
           }
        
        with open('o_2.nrg','r') as nrgFile:
            #Skip magic number
            nrgFile.readline()
            for line in nrgFile:
                tList=line.split()
                if "****" in tList[0]: break
        
                tLevel=EnergyLevel()
        
                if SET_DEBUG['prelevel']: print(tList)
        
                tLevel.index=pullValue(tList,'INT')
                tLevel.energy=pullValue(tList,'FLOAT')
                tLevel.g=pullValue(tList, 'FLOAT')
                tLevel.config=pullValue(tList)
                tLevel.term=pullValue(tList)               
        
                spec.levels.append(tLevel)
        
                #Make sure levels are in order
                if int(tLevel.index) != len(spec.levels):
                    raise Exception("Energy Levels out of order")
                
    
            if SET_DEBUG['postLevel']:    
                for level in spec.levels:
                    print(level.index,level.energy,level.g)
        

              
        with open('o_2.tp','r') as tpFile:
            #Skip magic number
            tpFile.readline()    
            for line in tpFile:
                tList=line.split()
                if "****" in tList[0]: break        
          
                isEina = False
        
                tbEina = pullValue(tList)        
                if tbEina == 'A': isEina=True
        
                tLo = pullValue(tList, 'INT')
                tHi = pullValue(tList, 'INT')
                tTP = pullValue(tList,'FLOAT')
                
                #print(tList)
        
                if len(tList)>0:
                    tType = pullValue(tList)
                else:
                    tType = None
         
                sKey = str(tLo) + ':' + str(tHi)
        
                if sKey in spec.transitions:
                    if isEina:
                        spec.transitions[sKey].eina.setTP(tTP, tType)                        
                    else:
                        raise Exception("Not Eina")
                else:        
                    tTran = Transition(spec.levels[tLo-1],spec.levels[tHi-1])
                    if isEina:
                        tTran.eina.setTP(tTP, tType)
                        spec.transitions[sKey]=tTran
                    else:
                        raise Exception("Not Eina")

        with open('o_2.coll','r') as collFile:
            #Skip magic number
            collFile.readline()     
            tTemps=collFile.readline().split()
            if pullValue(tTemps) != 'TEMP':
                raise Exception("Coll files should start with TEMP")
      
            for line in collFile:
                tList=line.split()
                if "****" in tList[0]:break
                if 'TEMP' in tList[0]:
                    raise Exception("Multiple temperature lines!!!")
                #print(tList)
          
                # Only supporting CS Electron at the moment        
                tx = pullValue(tList)
                if tx != 'CS':
                    raise Exception("NOT CS") 
                tx = pullValue(tList)        
                if tx != 'ELECTRON':
                    raise Exception("NOT ELECTRON")  
          
                #print(tList) 
          
                tLo = pullValue(tList, 'INT')         
                tHi = pullValue(tList, 'INT') 
          
                #print(tList)
          
                sKey = str(tLo) + ":" + str(tHi)
 
                spec.transitions[sKey].setCS(tTemps,tList)
    
    def writeStout(self):
        pass