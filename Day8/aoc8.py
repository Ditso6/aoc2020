file = "input.txt"

with open(file) as f:
	data = f.readlines()

programs = [line.rstrip() for line in data]

def run(programs):
	i = 0
	accumulator = 0
	operated = set()
	operations = [program.split() for program in programs]
	while i < len(programs):
		operation, operator = operations[i]
		operator = int(operator)

		if i in operated:
			return accumulator
			break

		operated.add(i)

		if operation == "jmp":
			i += operator

		elif operation == "nop":
			i += 1

		elif operation == "acc":
			accumulator += operator
			i += 1
	

answer1 = run(programs)
print(answer1)

programlist = []

for x in range(len(programs)):
	for program in programs:
		progs = []
		programcopy = programs[:]

		if "jmp" in programcopy[x]:
			program.replace("jmp", "nop", 1)

		elif "nop" in programcopy[x]:
			program.replace("nop", "jmp", 1)

		progs.append(programcopy)
	programlist.append(progs)

for program in programlist:
	if run(program) != 1930:
		print(run(program))
	
