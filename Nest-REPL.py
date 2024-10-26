# Variable arrays
var = [] 
vari = []

# Variables
parts = ""


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
        vari.append(variable)
        var.append(value)


# Functions used for the dictionary
def help_cmd(*args):
    help()

def get_variable_cmd(instruction):
    split = instruction.split()
    print(cmdStart + getVariable(str(split[1])))

def set_variable_cmd(instruction):
    split = instruction.split()
    setVariable(str(split[1]), str(split[2]))

def output_variable_cmd(instruction):
    split = instruction.split()
    print(cmdStart + str(getVariable(split[1])))

def close(*args):
    quit()


# Dictionary for command functions
commands = {
    "help": help_cmd,
    "getvar": get_variable_cmd,
    "setvar": set_variable_cmd,
    "output": output_variable_cmd,
    "exit": close,
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
