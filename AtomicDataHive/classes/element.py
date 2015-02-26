from classes.helpers import * #@UnusedWildImport
ELEMENT_NAMES = {}
ELEMENT_SYMBOLS = {}
ROMAN_NUMS = {1:"I",
              2:"II",
              3:"III",
              4:"IV",
              5:"V",
              6:"VI",
              7:"VII",
              8:"VIII",
              9:"IX",
              10:"X",
              11:"XI",
              12:"XII",
              13:"XIII",
              14:"XIV",
              15:"XV",
              16:"XVI",
              17:"XVII",
              18:"XVIII",
              19:"XIX",
              20:"XX",
              21:"XXI",
              22:"XXII",
              23:"XXIII",
              24:"XXIV",
              25:"XXV",
              26:"XXVI",
              27:"XXVII",
              28:"XXVIII",
              29:"XXIX",
              30:"XXX",
              }

SET_DEBUG={'preload':False}

#Preload element names and symbols
with open('ElementNames.txt','r') as File:
        for line in File:
            tList=line.split()
            Z = pullValue(tList, 'INT')
            symbol = pullValue(tList)
            name = pullValue(tList)
            
            ELEMENT_NAMES[Z] = name
            ELEMENT_SYMBOLS[Z] = symbol
            
if SET_DEBUG['preload']:
    for e in ELEMENT_NAMES.items():
        print(e)
    for e in ELEMENT_SYMBOLS.items():
        print(e)