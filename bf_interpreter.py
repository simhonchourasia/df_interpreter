import sys

# Get contents of file
file = open(sys.argv[1], "r")
program = file.read()
file.close()

# Hello world program from Wikipedia
program = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

# Initialize instruction pointer and memory
instPointer = 0
ram = [0]
memPointer = 0

while instPointer < len(program):
    instruction = program[instPointer]
    
    # >: Increment memory pointer
    if instruction == '>':
        memPointer += 1
        if len(ram) <= memPointer:
            ram.append(0)

    # <: Decrement memory pointer
    elif instruction == '<':
        memPointer -= 1
        if memPointer < 0:
            print("Memory error")
            sys.exit(0)

    # +: Increment byte at memory pointer
    elif instruction == '+':
        ram[memPointer] += 1
        # Wrap around
        if ram[memPointer] > 255:
            ram[memPointer] = 0

    # -: Decrement byte at memory pointer
    elif instruction == '-':
        ram[memPointer] -= 1
        # Wrap around
        if ram[memPointer] < 0:
            ram[memPointer] = 255

    # .: Output byte at memory pointer (as char)
    elif instruction == '.':
        print(chr(ram[memPointer]), end='')

    # ,: Input one byte and save to byte at memory pointer
    elif instruction == ',':
        ram[memPointer] = ord(input()[0]) % 256

    # [: If byte at memory pointer is zero, jump forward to matching ]
    elif instruction == '[':
        if ram[memPointer] == 0:
            numParens = 0
            instPointer += 1
            searching = True
            while instPointer < len(program) and searching:
                if program[instPointer] == '[':
                    numParens += 1
                elif program[instPointer] == ']':
                    if numParens == 0:
                        searching = False
                    else:
                        numParens -= 1

                instPointer += 1

    # ]: If byte at memory pointer is nonzero, jump back to the command after the matching [
    elif instruction == ']':
        if ram[memPointer] != 0:
            numParens = 0
            instPointer -= 1
            searching = True
            while instPointer >= 0 and searching:
                if program[instPointer] == ']':
                    numParens += 1
                elif program[instPointer] == '[':
                    if numParens == 0:
                        searching = False
                    else:
                        numParens -= 1

                instPointer -= 1

    # Proceed to next instruction
    instPointer += 1
