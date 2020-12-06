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


def search_mad_id(file):
    with open(file, "rt") as file:
        max_id = -1
        for line in file:
            line = line.strip()
            row, col, id = parse_boarding_pass(line)
            if id > max_id:
                max_id = id
        print(max_id)


search_mad_id("data/day5input")
