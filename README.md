# df_interpreter
An interpreter for the DF language. Turing complete and a pain to write in. 

## How to use it
After downloading, navigate to the folder in the command line, which should contain df_interpreter.py and the file you wish to run as a txt file, for example df_helloworld.txt. Then, in the command line, type in "python df_interpreter.py df_helloworld.txt". The results will appear in the command line. 

## Instructions
You can find these in the df_interpreter.py file. They're designed to make coding anything more than a simple hello world program take a great deal of effort to write. 

The values of register A, register B, instruction pointer, and memory pointer all start at 0. The memory is initialized to only contain 0, at address 0

* [space]: Reset register A to 0. 
* 1: Save byte at memory pointer to register A. 
* 2: Save byte at registerB to byte at memory pointer. 
* 3: Add byte at memory pointer to the byte at register A, save at register B. Then, switch the byte at memory pointer with the byte at register A. 
* 4: Cycle the bytes at register A, register B, and memory pointer. 
* 5: Add 19 to the byte at register A, mod 256. 
* 6: Add natToInt(registerA) to the instruction pointer; natToInt is defined as follows: if registerA even, natToInt(registerA) = registerA / 2. If registerA odd, natToInt(registerA) = -(registerA+1)/2)
* 7: Subtract byte at memory pointer from the byte at register B, store in register BB, and take the result mod 256. 
* 8: Take one byte of input and save to register A (as number from 0-255). 
* 9: Output the byte of input at register A (as char)
* 0: Conditional statement. Skips the next 21 instructions if the byte at memoryPointer is prime
* \`: Add natToInt(registerA) to the memory pointer; natToInt is defined as follows: if registerA even, natToInt(registerA) = registerA / 2. If registerA odd, natToInt(registerA) = -(registerA+1)/2). Handles out of memory issues. 
* d: Hardcoded to print "Hello "
* f: Hardcoded to print "World!"

Any other character given as instruction will do nothing. This can be useful. 
