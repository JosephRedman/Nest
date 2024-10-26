# Interpret a .nst file when provided.

file_path = "TestProg.nst"  # Replace with your file path

# Set up the array to store variables
var = [] 
vari = []

# Variables
parts = ""


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

def readLine(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.strip()  # Remove leading and trailing whitespace, including newline



def get_variable(instruction):
    split = instruction.split()
    print(getVariable(str(split[1])))

def set_variable(instruction):
    split = instruction.split()
    variable = split[1]
    value = " ".join(split[2:])  # Join everything after split[1] to form the full value
    setVariable(variable, value)

def output_variable(instruction):
    split = instruction.split()
    print(str(getVariable(split[1])))

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

functions = {

    "getvar": get_variable,
    "setvar": set_variable,
    "output": output_variable,
    "exit": close,
    "add": add,
    "sub": subtract,
    "mult": multiply,
    "div": divide,

}

for line in readLine(file_path):
    instruction = line
    if instruction:  # Check if the instruction is not empty
        command_key = instruction.split()[0].lower()  # Get the command part of the input
        # Execute command if it exists in the dictionary
        if command_key in functions:
            functions[command_key](instruction)  # Pass the instruction to the function
        else:
            print("SYNTAX ERROR: '" + instruction + "' IS NOT A VALID COMMAND OR FUNCTION. ENTER HELP FOR HELP")
    else:
        pass
