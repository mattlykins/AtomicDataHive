import traceback
## Convert wavenumbers to angstroms
def wavenumberToAngstrom(wavenumbers):
    return 1e8/wavenumbers
## Convert angstroms to wavenumbers 
def angstromToWavenumber(angstroms):
    return 1e8/angstroms

## Determine if the value, \p x, is an integer
# @param x This could be a string version of a number or a number
def is_int(x):
    # Can a string be converted to a number
    value = is_number(x)
    # If so, is this value an integer?
    if float.is_integer(value) == True:
        return int(value)
    else:
        raise TypeError("%s is not an integer" % x)
            
## Check to see if string, \p x, can be converted to a number
def is_number(x):
    try:
        value = float(x)
        return value
    except ValueError:
        raise ValueError("%s is not a number" % x)
        
## Pop the first value of a the list, \p tList, and return it
# @param tList The input list
# @param sType The expected value type to return. Optional for string
def pullValue(tList,sType=None):
    try:
        ppd = tList.pop(0)
    except IndexError:
        print("-"*80)
        traceback.print_stack()
        raise IndexError("-"*80)
        
    if sType == 'INT':
        is_int(ppd)
        return int(ppd)
    elif sType == 'FLOAT':
        is_number(ppd)
        return float(ppd)
    elif sType == 'STRING' or sType == None:
        return ppd
    else:
        raise ValueError("Invalid type %s",sType)