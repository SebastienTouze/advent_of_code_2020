# Sébastien Touzé
# Script for Advent Of Code 2020
# DAY 06

# We could do a trick here using a dictionary to keep unique keys then back to string, but it's king of python magic,
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


def keep_common_letters(ref_list, new_list):
    res = ref_list.copy()  # /!\ because Python affectation is reference affectation Youhou =.=
    for char in ref_list:
        if char not in new_list:
            res.remove(char)
    return res


def parse_input_print_result_p1(file):
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


def parse_input_print_result_p2(file):
    with open(file, "rt") as file:
        possible_answers = []
        new_group = True
        total = 0
        for line in file:
            line = line.strip()
            if len(line) > 0:
                if new_group:
                    new_group = False
                    possible_answers[:] = line
                else:
                    line_char_list = []
                    line_char_list[:] = line
                    possible_answers = keep_common_letters(possible_answers, line_char_list)
            else:
                total += len(possible_answers)
                possible_answers = []
                new_group = True
        total += len(possible_answers)
        print(total)


print("** Test (part 1, expected: 11) **")
parse_input_print_result_p1("data/day6test")

print("** Real **")
parse_input_print_result_p1("data/day6input")

print("** Test (part 2, expected: 6) **")
parse_input_print_result_p2("data/day6test")

print("** Real **")
parse_input_print_result_p2("data/day6input")
