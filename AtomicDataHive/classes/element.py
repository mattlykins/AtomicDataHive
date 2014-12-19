class element(object): 
    _unq_id=set()
    _unq_z =set()
    name=""
    symbol=""
    _atomicnumber=-1
    
      
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol
        if symbol in element._unq_id:
            raise ValueError("Duplicate element symbol: %s" % symbol)
        else:
            element._unq_id.add(symbol)
        
        self._atomicnumber = -1
        
    ## Prevent objects from getting new attributes
    def __setattr__(self, name, value):
        if hasattr(self, name):
            object.__setattr__(self, name, value)
        else:
            raise TypeError('Cannot set name %r on object of type %s' % (name, self.__class__.__name__))
        
        
    @property
    def atomicnumber(self):
        return self._atomicnumber
         
    @atomicnumber.setter
    def atomicnumber(self,Z):
        self._atomicnumber = int(Z)
        if Z != -1 and Z in element._unq_z:
            raise ValueError("Duplicate atomic number: %i" % Z)
        else:
            element._unq_z.add(Z)

    