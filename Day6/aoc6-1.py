file = "input.txt"

groupforms = []
forms = []
uniquegroupanswers = []
counts = []

with open(file) as f:
	data = f.read()

lines = data.split("\n\n")

for line in lines:
	form = list(line.replace("\n", ""))
	groupforms.append(form)

for groupform in groupforms:
	uniqueanswers = set(groupform)
	uniquegroupanswers.append(uniqueanswers)

for uniquegroupanswer in uniquegroupanswers:
	count = len(uniquegroupanswer)
	counts.append(count)

print(sum(counts))