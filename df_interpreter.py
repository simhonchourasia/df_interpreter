import sys

# Get contents of file
file = open(sys.argv[1], "r")
program = file.read()
file.close()

# Sample hello world program
program = "df"

# Initialize registers and memory
instPointer = 0
memPointer = 0
registerA = 0
registerB = 0
ram = [0]

# Helper functions

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i+=1
    return True

def natToInt(n):
    if n%2:
        return (-1)*(n+1)//2
    else:
        return n//2


# Interpreter

while instPointer < len(program):
    instruction = program[instPointer]

    # [space]: Reset register A to 0
    if instruction == ' ':
        registerA = 0

    # 1: Save byte at memory pointer to register A
    if instruction == '1':
        registerA = ram[memPointer]

    # 2: Save byte at registerB to byte at memory pointer
    if instruction == '2':
        ram[memPointer] = registerB

    # 3: Add byte at memory pointer to the byte at register A, save at register B
    # Then, switch the byte at memory pointer with the byte at register A
    if instruction == '3':
        registerB = ram[memPointer] + registerA
        registerA, ram[memPointer] = ram[memPointer], registerA

    # 4: Cycle the bytes at register A, register B, and memory Pointer
    #
    if instruction == '4':
        registerA, registerB, ram[memoryPointer] = registerB, ram[memoryPointer], registerA

    # 5: Add 19 to the byte at register A, mod 256
    if instruction == '5':
        registerA = (registerA + 19) % 256 # Tip: 513 = 19*27, and is 1 (mod 256)

    # 6: Add natToInt(registerA) to the instruction pointer; natToInt is defined as follows: 
    # if registerA even, natToInt(registerA) = registerA / 2
    # if registerA odd, natToInt(registerA) = -(registerA+1)/2)
    if instruction == '6':
        instPointer += natToInt(registerA)

    # 7: Subtract byte at memory pointer from the byte at register B, store in register B
    # Take the result mod 256
    if instruction == '7':
        registerB = (registerB - ram[memPointer]) % 256

    # 8: Take one byte of input and save to register A (as number from 0-255)
    if instruction == '8':
        registerA = ord(input()[0]) % 256

    # 9: Output the byte of input at register A (as char)
    if instruction == '9':
        print(chr(registerA), end='')

    # 0: Conditional statement. Skips the next 21 instructions if the byte at memoryPointer is prime
    if instruction == '0':
        if isPrime(ram[memPointer]):
            instPointer += 21

    # `: Add natToInt(registerA) to the memory pointer; natToInt is defined as follows: 
    # if registerA even, natToInt(registerA) = registerA / 2
    # if registerA odd, natToInt(registerA) = -(registerA+1)/2)
    # Handles out of memory issues
    if instruction == '`':
        memPointer += natToInt(registerA)
        if memPointer < 0:
            memPointer = 0
        if memPointer > len(ram):
            ram = ram + [0 for i in range(memPointer - len(ram))]

    # Hardcoded hello world
    if instruction == 'd':
        print("Hello ", end='')
    if instruction == 'f':
        print("World!", end='')


    # If register A is 6 mod 8, switch its value with register B
    if registerA % 8 == 6:
        registerA, registerB = registerB, registerA
    # Proceed to next instruction
    instPointer += 1
