# Sébastien Touzé
# Script for Advent Of Code 2020
# DAY 02
import re


def process_password_part1(mini, maxi, letter, password):
    p = re.compile(letter)
    test = p.findall(password)
    return int(mini) <= len(test) <= int(maxi)


def extract_data_from_line(line):
    p = re.compile('^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$')
    res = p.findall(line)
    return res[0]


def process_password_part2(pos1, pos2, letter, password):
    if int(pos1) > len(password) or int(pos2) > len(password):
        print("Warning: password too short to test rules, assuming false")
        return False
    return (letter == password[int(pos1) - 1]) ^ (letter == password[int(pos2) - 1])


#############
# Quick test
#############
test_line = '14-15 v: hvhvlhvvvwxvdvscdpvg'
test_extract = extract_data_from_line(test_line)
validity = process_password_part1(*test_extract)
validity2 = process_password_part2(*test_extract)
print("Test : this should be False: " + str(validity))
print("Test : this should be True: " + str(validity2))

#######
# Part1
#######
number_of_valid_passwords_part1 = 0
with open("data/day2input", "rt") as file:
    for line in file:
        line = line.strip()
        number_of_valid_passwords_part1 += 1 if process_password_part1(*(extract_data_from_line(line))) else 0

print("Number of valid passwords according to part1 rules: " + str(number_of_valid_passwords_part1))

#########
# Part 2
#########
number_of_valid_passwords_part2 = 0
with open("data/day2input", "rt") as file:
    for line in file:
        line = line.strip()
        number_of_valid_passwords_part2 += 1 if process_password_part2(*(extract_data_from_line(line))) else 0

print("Number of valid passwords according to part2 rules: " + str(number_of_valid_passwords_part2))
