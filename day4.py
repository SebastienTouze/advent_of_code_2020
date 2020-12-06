# Sébastien Touzé
# Script for Advent Of Code 2020
# DAY 04

import re


def analyse_passport(passport):
    p_ecl = re.compile("ecl:(amb|blu|brn|gry|grn|hzl|oth)")
    p_pid = re.compile("pid:[0-9]{9} ")
    p_eyr = re.compile("eyr:20((2[0-9])|30)")
    p_hcl = re.compile("hcl:#[0-9a-f]{6}")
    p_byr = re.compile("byr:(19[2-9][0-9])|(200[0-2])")
    p_iyr = re.compile("iyr:20(1[0-9]|20)")
    p_hgt = re.compile("hgt:((1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in))")
    return p_ecl.search(passport) and \
           p_pid.search(passport) and \
           p_eyr.search(passport) and \
           p_hcl.search(passport) and \
           p_byr.search(passport) and \
           p_iyr.search(passport) and \
           p_hgt.search(passport)


def parse_input_print_result(file):
    with open(file, "rt") as file:
        passport = ""
        nb_valid = 0
        total=0
        for line in file:
            line = line.strip()
            if len(line) > 0:
                passport += line + " "
            else:
                total += 1
                nb_valid += 1 if analyse_passport(passport) else 0
                passport = ""
        total += 1
        nb_valid += 1 if analyse_passport(passport) else 0
        print("Number of valid passports (or thing that is almost a passport): " + str(nb_valid) + "/" + str(total))


print("**Testing**")
parse_input_print_result("data/day4testp2invalid")
parse_input_print_result("data/day4testp2valid")

print("**Real data**")
parse_input_print_result("data/day4input")
