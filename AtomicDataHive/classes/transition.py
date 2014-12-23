from classes.energylevel import EnergyLevel
from classes.collision import collision

## Store transition probabilities by transition type
class tranProb(object):
    
    ## Initialize all tps to zero
    def __init__(self):
        self.E1=0.0
        self.E2=0.0
        self.E3=0.0
        self.M1=0.0
        self.M2=0.0
        self.M3=0.0
        
                    
    ## Set the tp for a given type
    # @param value The Einstein A for the transition type
    # @param tType String denoting the transition type. Not required for electric dipole
    def setTP(self,value,tType=None):
        if tType == 'E2':self.E2=value
        elif tType == 'E3':self.E3=value
        elif tType == 'M1':self.M1=value
        elif tType == 'M2':self.M2=value
        elif tType == 'M3':self.M3=value
        elif tType == None or tType == 'E1':self.E1=value
        else:
            print("%s is unknown type" % tType)
            #raise ValueError("%s is unknown type" % tType)
    
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
    ## Construct a transition
    # @param lo The energy level object of the lower level
    # @param hi The energy level object of the upper level
    def __init__(self,lo=EnergyLevel(),hi=EnergyLevel()):
        self.lo=lo
        self.hi=hi
        
        self.gf = -1.0
        self.energy = -1.0
        self.linestrength = -1.0
        
        self.collision = collision()
        
        
        # Set the default Einstein As and transition energies to -1
        self.eina=tranProb()
        if(lo.energy==hi.energy and lo.g==hi.g):
            raise Exception("Transition from the same levels")
        else:
            self.energy=hi.energy-lo.energy      

            
    ## Print the contents of the given transition
    def print(self):
        print("Lower Level: ",self.lo.index,self.lo.energy,self.lo.g,self.lo.config,self.lo.term)
        print("Upper Level: ",self.hi.index,self.hi.energy,self.hi.g,self.hi.config,self.hi.term)
        print("Energy: ",self.energy)
        self.eina.print()
#         tTemps = sorted(self.CS,key=lambda k: int(k) if k.isdigit() else float('-inf'))
#         print("Temps",tTemps)
#         tCS=[]
#         for t in tTemps:
#             tCS.append(self.CS[t])
#         print("CS",tCS)
