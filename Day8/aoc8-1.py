file = "input.txt"

with open(file) as f:
	data = f.readlines()
programs = [line.rstrip() for line in data]

def run():
	i = 0
	accumulator = 0
	operated = set()
	operations = []
	for program in programs:
		operation = program.split()
		operations.append(operation)
	"""operations = [program.split() for program in programs]"""

	while 0 <= i < len(programs):
		operation, operator = operations[i]
		operator = int(operator)

		if i in operated:
			print(accumulator)
			break

		operated.add(i)

		if operation == "jmp":
			i += operator

		elif operation == "nop":
			i += 1

		elif operation == "acc":
			accumulator += operator
			i += 1

run()
