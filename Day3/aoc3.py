def get_trees(slope, slope_right, slope_down):
    trees = 0
    for i, line in enumerate(slope[::slope_down]):
        if line[(i * slope_right) % len(line)] == '#':
            trees += 1
    return trees

def get_trajectorie(puzzle_input):
    slopes = [(3, 1)]

    solution = 1

    for slope in slopes:
        solution *= get_trees(puzzle_input, *slope)

    return solution

def get_trajectories(puzzle_input):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

    solution = 1

    for slope in slopes:
        solution *= get_trees(puzzle_input, *slope)

    return solution


with open('input.txt') as f:
    input = f.read()

puzzle_input = input.splitlines()


print("Antwoord deel 1: ", get_trajectorie(puzzle_input))
print("antwoord deel 2: ", get_trajectories(puzzle_input))