file = "input.txt"

with open(file) as f:
	data = f.readlines()

programs = [line.rstrip() for line in data]
operations = [program.split() for program in programs]

i = 0
accumulator = 0
operated = set()

while i < len(programs):
	operation, operator = operations[i]
	operator = int(operator)

	if i in operated:
		break

	operated.add(i)

	if operation == "jmp":
		i += operator

	elif operation == "nop":
		i += 1
	elif operation == "acc":
		accumulator += operator
		i += 1

print(accumulator)