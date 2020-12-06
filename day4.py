# Sébastien Touzé
# Script for Advent Of Code 2020
# DAY 04

import re


def analyse_passport(passport):
    p_ecl = re.compile("ecl")
    p_pid = re.compile("pid")
    p_eyr = re.compile("eyr")
    p_hcl = re.compile("hcl")
    p_byr = re.compile("byr")
    p_iyr = re.compile("iyr")
    p_hgt = re.compile("hgt")
    return p_ecl.search(passport) and p_pid.search(passport) and p_eyr.search(passport) and p_hcl.search(passport) and p_byr.search(passport) and p_iyr.search(passport) and p_hgt.search(passport)


def parse_input_print_result(file):
    with open(file, "rt") as file:
        passport = ""
        nb_valid = 0
        for line in file:
            line = line.strip()
            if len(line) > 0:
                passport += line + " "
            else:
                nb_valid += 1 if analyse_passport(passport) else 0
                passport = ""
        nb_valid += 1 if analyse_passport(passport) else 0
        print("Number of valid passports (or thing that is almost a passport): " + str(nb_valid))


print("**Testing**")
parse_input_print_result("data/day4test")

print("**Real data**")
parse_input_print_result("data/day4input")
