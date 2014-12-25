import pprint
class collision:
    collDataTypes = ['CSE',
                 'CSP',
                 'RE',
                 'RP',
                 'RH',
                 'RHE',
                 'RHE+',
                 'RHE+2',                 
                 'RH2-O',
                 'RH2-P',
                 'RH2'                    
                 ]  
    
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