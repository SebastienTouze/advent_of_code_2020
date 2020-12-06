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

    result = [['*']*line_size for i in range(nb_lines)]
    i = 0
    with open("data/day3input", "rt") as file:
        for line in file:
            line = line.strip()
            for j in range(0, len(line)):
                result[i][j] = line[j]
            i += 1

    return result, nb_lines


def move(matrix, slope, x, y):
    x = (x + slope[0]) % len(matrix[x])
    y += slope[1]
    return x, y, '#' == matrix[y][x]


def test_slope(matrix, matrix_end, slope_to_test):
    current_x, current_y = 0, 0
    encountered_trees = 0
    while current_y < matrix_end - 1:
        current_x, current_y, on_a_tree = move(matrix, slope_to_test, current_x, current_y)
        if on_a_tree:
            encountered_trees += 1
    return encountered_trees


# Initial position
matrix, destination = load_matrix()

slopes = ([1, 1], [3, 1], [5, 1], [7, 1], [1, 2])

solution = 1
for s in slopes:
    res = test_slope(matrix, destination, s)
    print("For slope right " + str(s[0]) + " and down " + str(s[1]) + ", result is " + str(res) + " trees encountered")
    solution = solution * res

print("Final result : " + str(solution))
