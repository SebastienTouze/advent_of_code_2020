# Sébastien Touzé
# Script for Advent Of Code 2020
# DAY 03

def load_matrix():
    nb_lines = 0
    line_size = 0
    with open("data/day3input", "rt") as file:
        nb_lines = sum(1 for _ in file)
        file.seek(0, 0)
        for line in file:
            line = line.strip()
            line_size = len(line)
            break

    res = [['*']*line_size for  i in range(nb_lines)]
    i = 0
    with open("data/day3input", "rt") as file:
        for line in file:
            line = line.strip()
            for j in range(0, len(line)):
                res[i][j] = line[j]
            i += 1

    return res, nb_lines


def move(matrix, x, y):
    x = (x + 3) % len(matrix[x])
    y += 1
    return x, y, '#' == matrix[y][x]


# Initial position
current_x, current_y = 0, 0
encountered_trees = 0
matrix, destination = load_matrix()

while current_y < destination - 1:
    current_x, current_y, on_a_tree = move(matrix, current_x, current_y)
    if on_a_tree:
        encountered_trees += 1

print(encountered_trees)
