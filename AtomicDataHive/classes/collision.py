class collision:
    colliders = ['ELECTRON',
                  'PROTON'
                   'H',
                   'HE',
                   'HE+',
                   'HE+2',
                   'H2',
                   'H2-ORTHO',
                   'H2-PARA'
                   ]
   
    
    def __init__(self):
        ## collData Dictionary storing collData lists with collDataType as key
        # collData list's first value is the name key of the associated temp
        self._collData = {}
        ## temps Dictionary that sorts temperature lists with a name key
        self._temps = {}    
    
    @property
    def collData(self):
        return self._collData
    
    @collData.setter
    def collData(self, collData):
            self._collData = collData
                
    @property
    def temps(self):
        return self._temps
    
    @temps.setter
    def temps(self, temp):
        self._temps = temp
        
        
        
        
