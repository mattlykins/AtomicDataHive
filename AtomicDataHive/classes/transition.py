from classes.energylevel import EnergyLevel

## Store transition probabilities by transition type
class tranProb(object):
    
    ## Initialize all tps to zero
    def __init__(self):
        pass
                    
    ## Set the tp for a given type
    # @param value The Einstein A for the transition type
    # @param tType String denoting the transition type. Not required for electric dipole
    def setTP(self,value,tType=None):
        if tType == 'E2':self.E2=value
        elif tType == 'E3':self.E3=value
        elif tType == 'M1':self.M1=value
        elif tType == 'M2':self.M2=value
        elif tType == 'M3':self.M3=value
        elif tType == None:self.E1=value
        else: raise ValueError("%s is unknown type" % tType)
    
    ## Print a list of the transition probabilities
    def print(self):
        print("E1: %e" % self.E1)
        print("E2: %e" % self.E2)
        print("E3: %e" % self.E3)
        print("M1: %e" % self.M1)
        print("M2: %e" % self.M2)
        print("M3: %e" % self.M3)

## Store data related to transitions
class Transition(object):
    lo = None
    hi = None
    CS = {}
    eina = None
    gf = -1.0
    energy = -1.0
    ## Construct a transition
    # @param lo The energy level object of the lower level
    # @param hi The energy level object of the upper level
    def __init__(self,lo=EnergyLevel(),hi=EnergyLevel()):
        self.lo=lo
        self.hi=hi
        
        # Initialize the collision strength dictionary
        # Set the default Einstein As and transition energies to -1
        self.CS={}
        self.eina=tranProb()
        if(lo.energy==hi.energy and lo.g==hi.g):
            raise Exception("Transition from the same levels")
        else:
            self.energy=hi.energy-lo.energy
            
    ## Prevent objects from getting new attributes
    def __setattr__(self, name, value):
        if hasattr(self, name):
            object.__setattr__(self, name, value)
        else:
            raise TypeError('Cannot set name %r on object of type %s' % (name, self.__class__.__name__)) 
        
        
    ## Set the electron collision strength for a transition
    # @param tempList is a list of temperatures
    # @param csList is the corresponding list of collision strengths
    def setCS(self,tempList,csList):
        for temp,colstr in zip(tempList,csList):
            self.CS[temp]=float(colstr)
            
    ## Print the contents of the given transition
    def print(self):
        print("Lower Level: ",self.lo.index,self.lo.energy,self.lo.g,self.lo.config,self.lo.term)
        print("Upper Level: ",self.hi.index,self.hi.energy,self.hi.g,self.hi.config,self.hi.term)
        print("Energy: ",self.energy)
        self.eina.print()
        tTemps = sorted(self.CS,key=lambda k: int(k) if k.isdigit() else float('-inf'))
        print("Temps",tTemps)
        tCS=[]
        for t in tTemps:
            tCS.append(self.CS[t])
        print("CS",tCS)