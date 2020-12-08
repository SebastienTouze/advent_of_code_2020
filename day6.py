# Sébastien Touzé
# Script for Advent Of Code 2020
# DAY 06

# We could do a trick here using a dictionary to keep unique keys then back to strin, but it's king of python magic,
# let's keep things an algorithmic way
def delete_duplicate_letters(s):
    source = []
    res = []
    source[:] = s
    source.sort()
    prev_char = ""
    for char in source:
        if prev_char != char:
            res.append(char)
        prev_char = char
    return res


def parse_input_print_result(file):
    with open(file, "rt") as file:
        answers_concat = ""
        total = 0
        for line in file:
            line = line.strip()
            if len(line) > 0:
                answers_concat += line
            else:
                total += len(delete_duplicate_letters(answers_concat))
                answers_concat = ""
        total += len(delete_duplicate_letters(answers_concat))
        print(total)

print ("** Test (expected: 11) **")
parse_input_print_result("data/day6test")

print ("** Real **")
parse_input_print_result("data/day6input")
