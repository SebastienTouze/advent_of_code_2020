# Sébastien Touzé
# Script for Advent Of Code 2020
# DAY 04

def pass_letter_to_binary(letter):
    if letter == "F" or letter == "L":
        return 0
    else:
        return 1


def parse_boarding_pass(bpass):
    row = 0
    for i in range(0, 7):
        row += pow(2, i) * pass_letter_to_binary(bpass[6 - i])
    column = 0
    for j in range(0, 3):
        column += pow(2, j) * pass_letter_to_binary(bpass[9 - j])
    return row, column, row * 8 + column


def search_max_id(file):
    with open(file, "rt") as file:
        max_id = -1
        for line in file:
            line = line.strip()
            row, col, id = parse_boarding_pass(line)
            if id > max_id:
                max_id = id
        print(max_id)


def check_all_seats(file, ids):
    with open(file, "rt") as file:
        for line in file:
            line = line.strip()
            id_occupied = (parse_boarding_pass(line))[2]
            ids[id_occupied] = 1
        return ids


def find_my_seat(ids):
    for i in range(1, len(ids)):
        if 0 == ids[i] and 1 == ids[i+1] and 1 == ids[i - 1]:
            return i
    return 0


print('Part 1 : printing max seat ID')
search_max_id("data/day5input")

print('Part 2 : finding my seat ID')
print(find_my_seat(check_all_seats("data/day5input", [0] * (127 * 8 + 7))))
