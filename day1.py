# Script for Avent Of Code 2020
# DAY 01

def day1(report):
    for index, num1 in enumerate(report[:len(report) - 2]):
        for num2 in report[index+1:len(report)-1]:
            if 2020 == num1 + num2:
                return num1 * num2


def day1part2(report):
    for index, num1 in enumerate(report[:len(report) - 3]):
        for num2 in report[index+1:len(report)-2]:
            for num3 in report[index+2:len(report)-1]:
                if 2020 == num1 + num2 + num3:
                    return num1 * num2 * num3


testInput = [1721, 979, 366, 299, 675, 1456]
with open("day1input", "rt") as file:
    inputFile = [int(line.strip()) for line in file]

print(inputFile)
print(day1(inputFile))
print(day1part2(inputFile))
