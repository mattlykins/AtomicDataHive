from classes.species import *
from classes.energylevel import EnergyLevel
from classes.transition import Transition
from classes.helpers import * #@UnusedWildImport
from classes.element import *
from classes.sql import *

import os.path,re

collDataStout = {('CS ELECTRON',0,'ELECTRON'),
             ('CS PROTON',0,'PROTON'),
             ('RATE ELECTRON',1,'ELECTRON'),
             ('RATE PROTON',1,'PROTON'),
             ('RATE H',1,'H'),
             ('RATE HE'),
             ('RATE HE+'),
             ('RATE HE+2'),
             ('RATE H2'),
             ('RATE H2 ORTHO'),
             ('RATE H2 PARA')                    
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
                if 'CSELECTRON' == tList[0].upper():
                    # CS ELECTRON or CSELECTRON 
                    cDataTypeIndex = 0
                    # Pop off CSELECTRON or CS and ELECTRON
                    pullValue(tList)                
                elif 'CS ELECTRON' == (tList[0] + " " + tList[1]).upper():
                    cDataTypeIndex = 0
                    # Pop off CSELECTRON or CS and ELECTRON
                    pullValue(tList)  
                    pullValue(tList)   
                elif 'CS PROTON' == (tList[0] + " " + tList[1]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 1
                elif 'RATE ELECTRON' == (tList[0] + " " + tList[1]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 2
                elif 'RATE PROTON' == (tList[0] + " " + tList[1]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 3                   
                elif 'RATE H' == (tList[0] + " " + tList[1]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 4     
                elif 'RATE HE' == (tList[0] + " " + tList[1]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 5 
                elif 'RATE HE+' == (tList[0] + " " + tList[1]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 6
                elif 'RATE HE+2' == (tList[0] + " " + tList[1]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 7
                elif 'RATE H2 ORTHO' == (tList[0] + " " + tList[1] + " " + tList[2]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 8                                    
                elif 'RATE H2 PARA' == (tList[0] + " " + tList[1] + " " + tList[2]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 9                    
                elif 'RATE H2' == (tList[0] + " " + tList[1]).upper():
                    pullValue(tList)
                    pullValue(tList)
                    cDataTypeIndex = 10
                else:
                    raise ValueError("Coll File reading unknown type:%s" % tList[0])
                                        
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
                    
                    
#             
#             if( dataType2 ):
#                 print("INT")
#             if dataType.upper() == 'CSELECTRON':
#                 lgCS = True
#                 lgColliders['Electron']=True
#             elif dataType.upper() == 'CS':
#                 lgCS = True
#             elif dataType.upper() == 'RATE':
#                 lgRate = True
#             elif dataType.upper() == 'TEMP':
#                 lgTemp = True
#             elif '******' in dataType:
#                 break
#             else:
#                 raise ValueError("Invalid term, %s, in %s" % (dataType,collFileName))
#             
#             print(dataType)
            
            

#         tTemps=collFile.readline().split()
#         if pullValue(tTemps) == 'TEMP':
#             for line in collFile:
#                 tList=line.split()
#                 if "****" in tList[0]:break
#                 
#                 if "#" in tList[0]: continue
#                 
#                 if 'TEMP' in tList[0]:
#                     tList.pop(0)
#                     tTemps = tList
#                     continue
#                 #print(tList)
#          
#                 # Only supporting CS Electron at the moment        
#                 tx = pullValue(tList)
#                 if tx != 'CS':
#                     print(tx)
#                     continue
#                     #raise Exception("NOT CS") 
#                 tx = pullValue(tList)        
#                 if tx != 'ELECTRON':
#                     continue
#                     #raise Exception("NOT ELECTRON")  
#          
#                 #print(tList) 
#                 
#                 # Determine what collision data is here using the unsplit and in
#                 # Loop over the split list, discarding non-ints and non-floats
#                 # Verify the proper # of values
#                 # Collisions need a class?
#          
#                 tLo = pullValue(tList, 'INT')         
#                 tHi = pullValue(tList, 'INT') 
#          
#                 #print(tList)
#          
#                 sKey = str(tLo) + ":" + str(tHi)
#     
#                 try:
#                     thisSpecies.transitions[sKey].setCS(tTemps,tList)
#                 except KeyError:
#                     #print("-"*60)
#                     #print(thisSpecies.stoutName,sKey)
#                     #print("-"*60)
#                     continue
    
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
        
    
    

        
    