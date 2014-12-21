from classes.species import *
from classes.energylevel import EnergyLevel
from classes.transition import Transition
from classes.helpers import * #@UnusedWildImport
from classes.element import *

import os.path,re
        
def readStout(thisSpecies,basePath):        
        
    SET_DEBUG={
       'prelevel':False,
       'postLevel':False,
       'preTP':False,
       'postTP':False,
       'preColl':False,
       'postColl':False
       }
    
    nrgFileName = basePath + thisSpecies.stoutName + ".nrg"
        
    with open(nrgFileName,'r') as nrgFile:
        #Skip magic number
        nrgFile.readline()
        for line in nrgFile:
            tList=line.split()
            if "****" in tList[0]: break
            
            if "#" in tList[0]: continue
    
            tLevel=EnergyLevel()
    
            if SET_DEBUG['prelevel']: print(tList)
    
            tLevel.index=pullValue(tList,'INT')
            tLevel.energy=pullValue(tList,'FLOAT')
            tLevel.g=pullValue(tList, 'FLOAT')
            if len(tList) > 1:
                tLevel.config=pullValue(tList)
                tLevel.term=pullValue(tList)               
    
            thisSpecies.levels.append(tLevel)
    
            #Make sure levels are in order
            if int(tLevel.index) != len(thisSpecies.levels):
                raise Exception("Energy Levels out of order")
            

        if SET_DEBUG['postLevel']:    
            for level in thisSpecies.levels:
                print(level.index,level.energy,level.g)
        

    tpFileName = basePath + thisSpecies.stoutName + ".tp"         
    with open(tpFileName,'r') as tpFile:
        #Skip magic number
        tpFile.readline()    
        for line in tpFile:
            tList=line.split()
            if "****" in tList[0]: break
            
            if "#" in tList[0]: continue      
      
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
    
            if sKey in thisSpecies.transitions:
                if isEina:
                    thisSpecies.transitions[sKey].eina.setTP(tTP, tType)                        
                else:
                    print("Not Eina")
                    continue
                    #raise Exception("Not Eina")
            else:        
                try:
                    tTran = Transition(thisSpecies.levels[tLo-1],thisSpecies.levels[tHi-1])
                    if isEina:
                        tTran.eina.setTP(tTP, tType)
                        thisSpecies.transitions[sKey]=tTran
                    else:
                        print("Not Eina")
                        continue
                        #raise Exception("Not Eina")
                except IndexError:
                    print("*"*60)
                    print(thisSpecies.stoutName,sKey)
                    print("*"*60)
                    continue
                
                
    collFileName = basePath + thisSpecies.stoutName + ".coll"
    with open(collFileName,'r') as collFile:
        #Skip magic number
        collFile.readline()     
        tTemps=collFile.readline().split()
        if pullValue(tTemps) == 'TEMP':
            for line in collFile:
                tList=line.split()
                if "****" in tList[0]:break
                
                if "#" in tList[0]: continue
                
                if 'TEMP' in tList[0]:
                    tList.pop(0)
                    tTemps = tList
                    continue
                #print(tList)
         
                # Only supporting CS Electron at the moment        
                tx = pullValue(tList)
                if tx != 'CS':
                    continue
                    #raise Exception("NOT CS") 
                tx = pullValue(tList)        
                if tx != 'ELECTRON':
                    continue
                    #raise Exception("NOT ELECTRON")  
         
                #print(tList) 
         
                tLo = pullValue(tList, 'INT')         
                tHi = pullValue(tList, 'INT') 
         
                #print(tList)
         
                sKey = str(tLo) + ":" + str(tHi)
    
                try:
                    thisSpecies.transitions[sKey].setCS(tTemps,tList)
                except KeyError:
                    print("-"*60)
                    print(thisSpecies.stoutName,sKey)
                    print("-"*60)
    
def writeStout():
    pass

def findStoutFiles():
    location = ".\\stout\\"
    # Generate list of paths
    # For stout, the 3 files will be in the same directory
    pathList = []
    for root, dirs, files in os.walk(location):
        for file in files:
            if file.endswith(".nrg"):
                pathList.append(os.path.join(root,file))
                
    return pathList




def importStout():    
    pathList = findStoutFiles()
    
    for path in pathList:
        filePath = os.path.split(path)
        basePath = filePath[0] + os.sep
        fileName = filePath[1]
        
        nameList = re.split('[_,.]',fileName)
        elemSymbol =pullValue(nameList)
        specIon = pullValue(nameList, 'INT')
        
        #Reverse dictionary lookup to find Z
        for Z, symbol in ELEMENT_SYMBOLS.items():
            if symbol.lower() == elemSymbol:
                elemZ = Z
        
        print(elemSymbol,elemZ,specIon,filePath[0])
        
        X = species(elemZ,specIon)
        readStout(X,basePath)
        