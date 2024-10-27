# Interpret a .nst file when provided.

file_path = "TestProg.nst"  # Replace with your file path

# Set up the array to store variables
var = [] 
vari = []

# Variables
acu1 = 0.0   # Accumilator 1 
acu2 = 0.0   # Accumilator 2. These are used instead of directly adding to variables and is good enough for now.

lineNum = 1

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

def readLine(file):
    global lineNum
    with open(file, 'r') as f:
        for line in f:
            yield line.strip()  # Remove leading and trailing whitespace, including newline
            lineNum = lineNum + 1


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
            print("SYNTAX ERROR ON LINE "+ str(lineNum) +": '" + instruction + "' IS NOT A VALID COMMAND OR FUNCTION.")
            print("FOR HELP, GO TO: https://github.com/JosephRedman/Nest/blob/main/README.md#currently-implemented")
    else:
        pass
