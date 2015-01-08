from classes.species import *
from classes.collision import *
from classes.energylevel import EnergyLevel
from classes.transition import Transition
from classes.helpers import * #@UnusedWildImport
from classes.element import *
from classes.sql import *

import os.path,re

colliders = collision.colliders
collDataTypes = collision.collDataTypes

# Dictionary where the key is Stout input for the type of collision.
# The value is a tuple. The first value is the associated index of collDataTypes
# The second value is the number of words that needs to be popped.
collDataStout = {'CS ELECTRON':(0,2),
                 'CSELECTRON':(0,1),
                 'CS PROTON':(1,2),
                 'RATE ELECTRON':(2,2),
                 'RATE PROTON':(3,2),
                 'RATE H':(4,2),
                 'RATE HE':(5,2),
                 'RATE HE+':(6,2),
                 'RATE HE+2':(7,2),                 
                 'RATE H2 ORTHO':(9,3),
                 'RATE H2 PARA':(10,3),
                 'RATE H2':(8,2)
                 }
        
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
            isGf = False
            isLineStrength = False
    
            tbCode = pullValue(tList)        
            if tbCode == 'A': isEina=True
            elif tbCode == 'S': isLineStrength=True
            elif tbCode == 'GF': isGf = True
            else: raise Exception("Must start with A, S, or GF")
    
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
                elif isLineStrength:
                    thisSpecies.transitions[sKey].linestrength = tTP
                elif isGf:
                    thisSpecies.transitions[sKey].gf = tTP                        
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
                    elif isLineStrength:
                        tTran.linestrength = tTP
                    elif isGf:
                        tTran.gf = tTP    
                    else:
                        print("Not Eina")
                        continue
                        #raise Exception("Not Eina")
                except IndexError:
                    #print("*"*60)
                    #print(thisSpecies.stoutName,sKey)
                    #print("*"*60)
                    continue
                
                
    collFileName = basePath + thisSpecies.stoutName + ".coll"
    with open(collFileName,'r') as collFile:
        #Skip magic number
        collFile.readline()
        
        numTemps = 0
        tempLabel = ''
        tempList = []
        
        for line in collFile:
            tList = line.split()
            if '****' in tList[0]: break
            if tList[0][0] == '#':continue
            #print(tList)
            
            
            if 'TEMP' == tList[0].upper():
                # Pop off TEMP
                pullValue(tList)
                #print(tList)
                tempList = tList
                
                #print(tList)
                
            else:
                inputString = ''
                dataTypeTuple = (-1,-1)
                for i in range(3,0,-1):
                    print("i = %i" %i)
                    inputString = tList[0]
                    
                    for j in range(1,i,1):
                        print("j = %i" %j)
                        inputString = inputString + ' ' + tList[j]
                                       
                    try:
                        print(inputString)
                        dataTypeTuple = collDataStout[inputString.upper()]
                        break
                    except:                       
                        continue 
                    
                    #raise ValueError("%s is not valid collision data type" % tList[0].upper())

                #print(dataTypeTuple)    
                
                cDataTypeIndex = dataTypeTuple[0]
                numToPop = dataTypeTuple[1]
                
                for i in range(numToPop):
                    print(pullValue(tList))
                #---------------------------------------                
                tLo = pullValue(tList, 'INT')         
                tHi = pullValue(tList, 'INT') 
       
                sKey = str(tLo) + ":" + str(tHi)
                #print(sKey,tList)
                 
                                
                 
                if sKey in thisSpecies.transitions:
                    cDataType = thisSpecies.transitions[sKey].collision.collDataTypes[cDataTypeIndex]
                    thisSpecies.transitions[sKey].collision.collData = [tempList, tList,cDataType]
                else:
                    try:
                        tTran = Transition(thisSpecies.levels[tLo-1],thisSpecies.levels[tHi-1])
                        thisSpecies.transitions[sKey]=tTran
                        cDataType = thisSpecies.transitions[sKey].collision.collDataTypes[cDataTypeIndex]
                        thisSpecies.transitions[sKey].collision.collData = [tempList, tList,cDataType]
                    except IndexError:
                        print("*"*60)
                        print(thisSpecies.stoutName,sKey)
                        print("*"*60)
                        continue                    

    
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
    
    dataSet = {}
    
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
        
        dataSet[X.stoutName] = X
        
    return dataSet

def dbStout(species):
    con = dbConnect('stout.db')
    c = dbCreate(con)
    
    speciesid = dbAddSpecies(c, species.elemName, species.Z, species.specIon)
    dbCommit(con)
    
    for x in species.levels:
        dbAddLevel(c, x.index, x.energy, x.g, speciesid)
        
    dbCommit(con)
    
    for key,T in species.transitions.items():
        transitionid = dbAddTransition(c, key, T.lo.index, T.hi.index, speciesid)
        print(transitionid)
        dbAddTransitionProbability(c, T.eina.E1, T.eina.E2, T.eina.E3, T.eina.M1, T.eina.M2, T.eina.M3, transitionid, speciesid)
        
    dbCommit(con)
        
    
    

        
    
