# Variable arrays
var = [] 
vari = []

# Variables
global acu1
global acu2

acu1 = 0.0   # Accumilator 1 
acu2 = 0.0   # Accumilator 2. These are used instead of directly adding to variables and is good enough for now.

cmdStart = "]"   # Edit this to change the line header
cmdStart = cmdStart + " "


# Functions used by the program
def helpUrl():
    print(cmdStart + "FOR HELP, GO TO: https://github.com/JosephRedman/Nest/blob/main/README.md#currently-implemented")

def getVariable(variable):
    i = 0
    while vari[i] != variable:
        i += 1
    return var[i]


def setVariable(variable, value):
    global acu1, acu2  # Allow modification of global variables acu1 and acu2
    
    if variable == "acu1":
        acu1 = getVariable(value)
    elif variable == "acu2":
        acu2 = getVariable(value)
    else:
        # Search for the variable in 'vari' and update if it exists
        for i in range(len(vari)):
            if vari[i] == variable:
                var[i] = value
                break
        else:
            # If the variable doesn't exist, add it to 'vari' and 'var'
            vari.append(variable)
            var.append(value)

# Functions used for the dictionary
def help(*args):
    helpUrl()

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

def get_value(val):
    # Helper function to get the float value of a variable or a number.
    if val == 'acu1':
        return float(acu1)
    elif val == 'acu2':
        return float(acu2)
    else:
        return float(val)

def add(instruction):
    split = instruction.split()
    val1 = get_value(split[1])
    val2 = get_value(split[2])
    ans = val1 + val2
    setVariable(split[3], ans)

def subtract(instruction):
    split = instruction.split()
    val1 = get_value(split[1])
    val2 = get_value(split[2])
    ans = val1 - val2
    setVariable(split[3], ans)

def multiply(instruction):
    split = instruction.split()
    val1 = get_value(split[1])
    val2 = get_value(split[2])
    ans = val1 * val2
    setVariable(split[3], ans)

def divide(instruction):
    split = instruction.split()
    val1 = get_value(split[1])
    val2 = get_value(split[2])
    ans = val1 / val2
    setVariable(split[3], ans)

# Dictionary for command functions
commands = {
    "getHelp": help,
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
            if instruction.split()[1:]:
                commands[command_key](instruction)
            else:
                commands[command_key]()
        else:
            print(cmdStart + "SYNTAX ERROR: '" + instruction + "' IS NOT A VALID COMMAND OR FUNCTION. ENTER HELP FOR HELP")
    else:
        pass

# Run the main function in a loop
while True:
    mainNoFile()
