import pprint
class collision:
    # List of lists that holds the id, isRate, and collider index
    # collider index refernces colliders list
    collDataTypes = [('CSE',False,0),
                 ('CSP',False,1),
                 ('RE',True,0),
                 ('RP',True,1), 
                 ('RH',True,2),
                 ('RHE',True,3),
                 ('RHE+',True,4),
                 ('RHE+2',True,5),                 
                 ('RH2-O',True,6),
                 ('RH2-P',True,7),
                 ('RH2',True,8)                   
                 ] 
    colliders = ['ELECTRON','PROTON','HYDROGEN','HELIUM','HELIUM+','HELIUM+2','HYDROGEN-ORTHO','HYDROGEN-PARA','MOLEHYDROGEN']     
    
    def __init__(self):
        ## collData Dictionary storing collData dictionaries with collDataType as key
        # collData list's first value is the name key of the associated temp
        self._collData = {}

    
    @property
    def collData(self):
        return self._collData
    
    @collData.setter
    def collData(self, inputTuple):
        temps = inputTuple[0]
        collData = inputTuple[1]
        dataType = inputTuple[2]
        
        tempDir = {}
        for t,coll in zip(temps,collData):
            tempDir[t] = coll
            
        self._collData[dataType] = tempDir