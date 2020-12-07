file = 'input.txt'
with open(file) as f:
	data = f.readlines()

rules = {}

for rule in data:
	bags, contents = rule.split("contain")
	bags = bags.strip()
	bags = bags.replace(" bags", "")
	if bags not in rules:
		rules[bags] = {}

	for colors_allowed in contents.split(","):
		if colors_allowed.strip()[:2] != "no":
			number = colors_allowed[1]
			color = colors_allowed[2::]
			color = color.strip()
			color = color.replace(".", "")
			color = color.replace(" bags", "")
			color = color.replace(" bag", "")
			if color not in rules[bags]:
				rules[bags][color] = 0
			rules[bags][color] += int(number)

answerbags = set()
answerbags.add('shiny gold')

for x in range(5):
	for rule in rules:
		for bag in rules[rule]:
			if bag in answerbags:
				answerbags.add(rule)

print(answerbags)
print(len(answerbags) - 1)