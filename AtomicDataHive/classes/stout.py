from classes.energylevel import EnergyLevel
from classes.transition import Transition
from classes.helpers import * #@UnusedWildImport
class stout():
    levels=[]
    transitions={}
    
    def __init__(self):
        pass

    ## Prevent objects from getting new attributes
    def __setattr__(self, name, value):
        if hasattr(self, name):
            object.__setattr__(self, name, value)
        else:
            raise TypeError('Cannot set name %r on object of type %s' % (name, self.__class__.__name__))
        
    def readStout(self):        
        
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
        
                stout.levels.append(tLevel)
        
                #Make sure levels are in order
                if int(tLevel.index) != len(stout.levels):
                    raise Exception("Energy Levels out of order")
                
    
            if SET_DEBUG['postLevel']:    
                for level in stout.levels:
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
        
                if sKey in stout.transitions:
                    if isEina:
                        stout.transitions[sKey].eina.setTP(tTP, tType)                        
                    else:
                        raise Exception("Not Eina")
                else:        
                    tTran = Transition(stout.levels[tLo-1],stout.levels[tHi-1])
                    if isEina:
                        tTran.eina.setTP(tTP, tType)
                        stout.transitions[sKey]=tTran
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
 
                stout.transitions[sKey].setCS(tTemps,tList)
    
    def writeStout(self):
        pass