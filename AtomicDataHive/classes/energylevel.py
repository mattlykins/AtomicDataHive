##Store energy level data
class EnergyLevel:
    ## Construct energy level
    # parameters can be set here or in individual methods
    def __init__(self,index=None,energy=None,g=None):
        self.energy=energy if energy is not None else -1
        self.g=g if g is not None else -1
        self.index=index if index is not None else -1
        
    ## Sets the index of the energy level
    # @param index The index of the energy level
    def setIndex(self,index):
        self.index=index
    ## Sets the energy of the level
    # @param energy The energy of the level in wavenumbers
    def setEnergy(self,energy):
        self.energy=energy  
    ## Sets the statistical weight of the level
    # @param g The statistical weight of the level in wavenumbers      
    def setG(self,g):
        self.g=g
        
    def setConfiguration(self,config):
        self.config=config
    
    def setTerm(self,term):
        self.term=term