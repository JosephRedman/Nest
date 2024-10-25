var = [] 
vari = [] 
parts = ""
cmdStart = "] "


def getVariable(variable):
    
    i = 0

    while vari[i] != variable:
        i = i +1
    return var[i]

def setVariable(variable, value):
    
    for i in range(len(vari)):
        if vari[i] == variable:
            var[i] = value
            break
    else:
        # If the loop completes without finding `variable`, add it to `vari` and `var`
        vari.append(variable)
        var.append(value)
    print(vari + var)



def mainNoFile():

    instruction = str(input(cmdStart))

    if "help" in instruction:

        print(cmdStart + "HELP:")
        print(cmdStart + "HELP   - THIS SCRIPT        - USAGE: HELP")
        print(cmdStart + "GETVAR - GETS A VARIABLE    - USAGE: GETVAR VAR")
        print(cmdStart + "SETVAR - SETS A VARIABLE    - USAVE: SETVAR VAR, VALUE")
        print(cmdStart + "OUTPUT - OUTPUTS A VARIABLE - USAVE: SETVAR VAR, VALUE")
    elif "getvar" in instruction:
        
        split = instruction.split()

        print(cmdStart + getVariable(str(split[1])))
    elif "setvar" in instruction:
        
        split = instruction.split()

        setVariable(str(split[1]), str(split[2]))
    elif "output" in instruction:
        
        split = instruction.split()

        print(cmdStart + str(getVariable(split[1])))


while True:
    mainNoFile()
