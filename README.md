# Nest
Nest is a custom programming language / REPL written in python but will be eventually be available in EXE form.
Nest is made with readability in mind so simple functions are used, for instance in the REPL, to easilly output a variable set, you just enter `getvar x` where x is the variable you need to know's value.
Nest has been designed to be similar to python without acctually being pyton itself (even though it is written in it!). Unless you are a variable, the language is NOT case-sensitive for ease of use.

---

## Help

### Maths
Nest has some simple built-in math functions:

`add`

`sub`

`mult`

`div`

You can use these with plain numbers, or with the accumulators . These are set with `setvar acu1 x` or `setvar acu2 x` where `x` is a pre-defined variable. When using the accumulators, the language assumes that the values given are numbers.

---

### Variables
Nest's variables are simple. To create a variable do `setvar x abc` Creates the variable `x` with the string abc inside. From then on `setvar x xyz` would just set `x` to the value given. In order to "get" a variable (usefull in REPL), just use `getvar x` where x is the variable. This throws an error if the variable does not exist.

---

### Outputs
To output to the console, use `output x` where `x` is a variable containing a string or a number etc

---
## To do:

- [ ] Loops
- [x] Outputs
- [x] Maths
- [x] Variables
- [ ] Arrays
- [ ] Functions
- [x] Comments

---

## Currently Implemented:

placeholders:

x = variable, y = value, acu1 = accumulator 1, acu2 = accumulator 2.

---

`getHelp` - shows the user a list of "commands" they can type in the REPL, will be replaced to a link here. **Does not work in programs**.

`getvar x` - "gets" a variable and outputs it's value to the console.

`setvar x y` - "sets" a variable to a certain value.

`output x` - Outputs a variable to the console.

`exit` - closes the REPL or exits the program.

`add y y x` - adds 2 numbers and sets a variable to the answer. The first value given is the first in the operation, so `add 5 10 x` does 5+10 and sets it to x

`sub y y x` - subtracts 2 numbers and sets a variable to the answer. The first value given is the first in the operation, so `sub 5 10 x` does 5-10 and sets it to x

`mult y y x` - multiplies 2 numbers and sets a variable to the answer. The first value given is the first in the operation, so `mult 5 10 x` does 5*10 and sets it to x

`div y y x` - divides 2 numbers and sets a variable to the answer. The first value given is the first in the operation, so `div 5 10 x` does 5/10 and sets it to x

---

### Acknowledgements

This code was fully written my me, Joseph, in my spare time, so errors and features may take time to be implemented. Thanks for understanding!

Thanks to @kolihinokami and @octacore4f on discord for suggestions in the James Sharman's Discord server for this language!
