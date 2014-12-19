from classes.helpers import * #@UnusedWildImport
##Store energy level data
class EnergyLevel(object):
    _index = -1
    _energy = -1
    _g = -1
    config = ""
    term = ""
    ## Construct energy level
    # parameters can be set here or in individual methods
    def __init__(self,index=None,energy=None,g=None):
        self.energy=energy if energy is not None else -1
        self.g=g if g is not None else -1
        self.index=index if index is not None else -1
        
    ## Prevent objects from getting new attributes
    def __setattr__(self, name, value):
        if hasattr(self, name):
            object.__setattr__(self, name, value)
        else:
            raise TypeError('Cannot set name %r on object of type %s' % (name, self.__class__.__name__))
        
    @property
    def index(self):
        return self._index
    
    ## Sets the index of the energy level
    # @param index The index of the energy level
    @index.setter
    def index(self,index):
        _x = is_int(index)
        self._index = _x
        
    @property
    def energy(self):
        return self._energy
    
    ## Sets the energy of the level
    # @param energy The energy of the level in wavenumbers
    @energy.setter
    def energy(self,energy):
        _x = is_number(energy)
        self._energy = _x   
        
    @property
    def g(self):
        return self._g
    
    ## Sets the statistical weight of the level
    @g.setter
    def g(self,g):
        _x = is_number(g)
        self._g = _x   
