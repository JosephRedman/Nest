# Variable arrays
var = [] 
vari = []


cmdStart = "]"   # Edit this to change the line header
cmdStart = cmdStart + " "


# Functions used by the program
def help():
    print(cmdStart + "HELP:")
    print(cmdStart + "HELP   - THIS SCRIPT           - USAGE: HELP")
    print(cmdStart + "GETVAR - GETS A VARIABLE       - USAGE: GETVAR VAR")
    print(cmdStart + "SETVAR - SETS A VARIABLE       - USAGE: SETVAR VAR, VALUE")
    print(cmdStart + "OUTPUT - OUTPUTS A VARIABLE    - USAGE: OUTPUT VAR")
    print(cmdStart + "EXIT   - EXIT THE REPL SESSION - USAGE: EXIT")


def getVariable(variable):
    i = 0
    while vari[i] != variable:
        i += 1
    return var[i]

def setVariable(variable, value):
    for i in range(len(vari)):
        if vari[i] == variable:
            var[i] = value
            break
    else:
        # If the loop completes without finding 'variable', add it to 'vari' and 'var'
        vari.append(variable)
        var.append(value)


# Functions used for the dictionary
def help(*args):
    help()

def get_variable(instruction):
    split = instruction.split()
    print(cmdStart + str(getVariable(str(split[1]))))

def set_variable(instruction):
    split = instruction.split()
    variable = split[1]
    value = " ".join(split[2:])  # Join everything after split[1] to form the full value
    setVariable(variable, value)

def output(instruction):
    split = instruction.split()
    print(cmdStart + str(getVariable(split[1])))

def close(*args):
    quit()

def add(instruction):
    split = instruction.split()
    ans = float(split[1]) + float(split[2])
    setVariable(split[3], ans)

def subtract(instruction):
    split = instruction.split()
    ans = float(split[1]) - float(split[2])
    setVariable(split[3], ans)

def multiply(instruction):
    split = instruction.split()
    ans = float(split[1]) * float(split[2])
    setVariable(split[3], ans)

def divide(instruction):
    split = instruction.split()
    ans = float(split[1]) / float(split[2])
    setVariable(split[3], ans)


# Dictionary for command functions
commands = {
    "help": help,
    "getvar": get_variable,
    "setvar": set_variable,
    "output": output,
    "exit": close,
    "add": add,
    "sub": subtract,
    "mult": multiply,
    "div": divide,
}

# Main function to process input
def mainNoFile():
    instruction = str(input(cmdStart)).strip()
    if instruction:  # Check if the instruction is not empty
        command_key = instruction.split()[0].lower()  # Get the command part of the input
        # Execute command if it exists in the dictionary
        if command_key in commands:
            commands[command_key](instruction)  # Pass the instruction to the function
        else:
            print(cmdStart + "SYNTAX ERROR: '" + instruction + "' IS NOT A VALID COMMAND OR FUNCTION. ENTER HELP FOR HELP")
    else:
        pass

# Run the main function in a loop
while True:
    mainNoFile()
