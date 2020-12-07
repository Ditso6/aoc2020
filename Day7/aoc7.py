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

	for colours_allowed in contents.split(","):
		if colours_allowed.strip()[:2] != "no":
			number = colours_allowed[1]
			colour = colours_allowed[2::]
			colour = colour.strip()
			colour = colour.replace(".", "")
			colour = colour.replace(" bags", "")
			colour = colour.replace(" bag", "")
			if colour not in rules[bags]:
				rules[bags][colour] = 0
			rules[bags][colour] += int(number)

answerbags = set()
answerbags.add("shiny gold")

for x in range(5):
	for rule in rules:
		for bag in rules[rule]:
			if bag in answerbags:
				answerbags.add(rule)
answerbags.remove("shiny gold")
print(answerbags)
print(len(answerbags))


def findcontent(bag_colour):
    count = 0
    for bag in rules[bag_colour]:
        bags = rules[bag_colour][bag]
        inside = findcontent(bag)
        count += bags + bags * inside

    return count


print(findcontent('shiny gold'))