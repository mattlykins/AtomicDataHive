class collision:
    colliders =['Electron',
                'Proton',
                'H0',
                'He0',
                'He+',
                'He+2',
                'H2',
                'H2 Ortho',
                'H2 Para'
                ]    
    
    def __init__(self):
        ## Store collision rates for all colliders
        ## Collision strengths for electron and proton
        self._strength = {}
        self.temperature = -1.0
        self._rate = {}
        
        
        ## Initialize all collider rates to -1 by passing a tuple
        for x in __class__.colliders:
            self.rate = (-1.0,x)
            self.strength = (-1.0,x)
            
    
    
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, vallider):
        for c in __class__.colliders:
            if c == vallider[1]:
                self._rate[vallider[1]] = float(vallider[0])
                
    @property
    def strength(self):
        return self._strenth
    
    @strength.setter
    def strength(self,vallider):
        for c in __class__.colliders:
            if c == vallider[1]:
                self._strength[vallider[1]] = float(vallider[0])
                
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, temp):
        if temp > 0.0 or -1.0:
            self._temperature = temp
        else:
            raise ValueError("Trying to set negative temperature")
        
        
        
        
