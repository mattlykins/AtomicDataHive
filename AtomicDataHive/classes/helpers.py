import sys, traceback
## Convert wavenumbers to angstroms
def wavenumberToAngstrom(wavenumbers):
    return 1e8/wavenumbers
## Convert angstroms to wavenumbers 
def angstromToWavenumber(angstroms):
    return 1e8/angstroms


def is_int(x):
    try:
        value = int(x)
        return value
    except ValueError:
        sys.exit("%s is not an int" % x)
        
def is_number(x):
    try:
        value = float(x)
        return value
    except ValueError:
        sys.exit("%s is not a number" % x)
        
def pullValue(tList,sType):
    try:
        ppd = tList.pop(0)
    except IndexError:
        print("-"*80)
        traceback.print_stack()
        sys.exit("-"*80)
        
    if sType == 'INT':
        is_int(ppd)
        return int(ppd)
    elif sType == 'FLOAT':
        is_number(ppd)
        return float(ppd)
    elif sType == 'STRING':
        return ppd
    else:
        sys.exit("You must specify type")