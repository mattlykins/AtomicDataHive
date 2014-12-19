import sys
from classes.energylevel import EnergyLevel

class tranProb():
    def __init__(self):
        self.E1=0.0
        self.E2=0.0
        self.E3=0.0
        self.M1=0.0
        self.M2=0.0
        self.M3=0.0
                
    def setTP(self,value,tType=None):
        if tType == 'E2':self.E2=value
        elif tType == 'E3':self.E3=value
        elif tType == 'M1':self.M1=value
        elif tType == 'M2':self.M2=value
        elif tType == 'M3':self.M3=value
        elif tType == None:self.E1=value
        else: sys.exit("setTP: %s is unknown type" % tType)
    
    def print(self):
        print("E1: %e" % self.E1)
        print("E2: %e" % self.E2)
        print("E3: %e" % self.E3)
        print("M1: %e" % self.M1)
        print("M2: %e" % self.M2)
        print("M3: %e" % self.M3)

## Store data related to transitions
class Transition():
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
        self.energy=-1.0       
        if(lo.energy==hi.energy and lo.g==hi.g):
            sys.exit("Transition from the same levels")
        else:
            self.energy=hi.energy-lo.energy
            
        
            
    
    ## Set the Einstein A for a transition
    # @param eina The transition's A value
    def setEinA(self,eina):
        self.eina=eina
        
        
    ## Set the electron collision strength for a transition
    # @param tempList is a list of temperatures
    # @param csList is the corresponding list of collision strengths
    def setCS(self,tempList,csList):
        for temp,colstr in zip(tempList,csList):
            self.CS[temp]=colstr
            
    def print(self):
        print("Lower Level: ",self.lo.index,self.lo.energy,self.lo.g)
        print("Upper Level: ",self.hi.index,self.hi.energy,self.hi.g)
        print("Energy: ",self.energy)
        self.eina.print()
        tTemps = sorted(self.CS,key=lambda k: int(k) if k.isdigit() else float('-inf'))
        print("Temps",tTemps)
        tCS=[]
        for t in tTemps:
            tCS.append(self.CS[t])
        print("CS",tCS)