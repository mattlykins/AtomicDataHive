from classes.element import * #@UnusedWildImport
class species(object):
    def __init__(self,Z,specIon):
        self.levels=[]
        self.transitions={}
        self.Z = Z
        self.specIon = specIon
        self.elemIon = specIon - 1
        self.elemName = ELEMENT_NAMES[self.Z]
        self.elemSymbol = ELEMENT_SYMBOLS[self.Z]
        self.spectrumName = self.elemSymbol + ROMAN_NUMS[self.specIon]
        self.ionName = self.elemSymbol + "+" + str(self.elemIon)
        self.stoutName =self.elemSymbol.lower() + "_" + str(self.specIon)