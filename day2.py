# Sébastien Touzé
# Script for Advent Of Code 2020
# DAY 02
import re


def process_password(mini, maxi, letter, password):
    p = re.compile(letter)
    test = p.findall(password)
    return int(mini) <= len(test) <= int(maxi)


def extract_data_from_line(line):
    p = re.compile('^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$')
    res = p.findall(line)
    return res[0]


test_line = '14-15 v: hvhvlhvvvwxvdvscdpvg'
test_extract = extract_data_from_line(test_line)
validity = process_password(*test_extract)
print("Test : this should be False: " + str(validity))

number_of_valid_passwords = 0
with open("data/day2input", "rt") as file:
    for line in file:
        line = line.strip()
        number_of_valid_passwords += 1 if process_password(*(extract_data_from_line(line))) else 0

print("Number of valid passwords : " + str(number_of_valid_passwords))
