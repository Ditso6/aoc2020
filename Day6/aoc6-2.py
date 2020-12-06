file = "input.txt"
with open(file) as f:
    data = f.read()
    lines = data.replace("\n"," ")
    groups = lines.split("  ")
 
answer_counter = 0

for group in groups:
    group = group.split(" ")
    persons = len(group)
    individual_answers = {}
    group_answers = []
    for individual_answer in group:
        for answer in individual_answer:
            if answer not in individual_answers:
                individual_answers[answer] = 1
            elif answer in individual_answers:
                individual_answers[answer] += 1
    for answers, times_occurred in individual_answers.items():
            if times_occurred == persons:
                group_answers.append(answers)
    answer_counter += (len(group_answers))
print(answer_counter)