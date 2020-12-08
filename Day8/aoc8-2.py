file = "input.txt"

with open(file) as f:
    data = f.readlines()
programs = [line.rstrip() for line in data]

def run(programs):
    i = 0
    accumulator = 0
    operated = set()
    """operations = []
    for program in programs:
        operation = program.split()
        operations.append(operation)"""
    """operations = [program.split() for program in programs]"""

    while 0 <= i < len(programs):
        operation, operator = programs[i]
        operator = int(operator)

        if i in operated:
            return 

        operated.add(i)

        if operation == "jmp":
            i += operator

            if i == len(programs):
                print(accumulator)
                return 

        elif operation == "nop":
            i += 1

        elif operation == "acc":
            accumulator += operator
            i += 1

def solve(programs):    
    prog = []
    for program in programs:
        operation, operator = program.split()
        prog.append([operation, int(operator)])

    progs = []
    for x in range(len(prog)):
        progcopy = prog[:]

        if (progcopy[x][0] in ["jmp"]):
            progcopy[x] = ["nop", progcopy[x][1]]
            progs.append(progcopy)
        
        elif (progcopy[x][0] in ["nop"]):
            progcopy[x] = ["jmp", progcopy[x][1]]
            progs.append(progcopy)

    for progf in progs:
        answer = run(progf)


solve(programs)


