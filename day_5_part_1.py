import array
import math
import re
import string


def get_file_data(file_name):
    f = open(file_name)

    file = []

    for line in f:
        file.append(line)

    rules = []
    idx = 0

    line = file[idx]
    while not line.isspace():
        rules.append(file[idx][0:-1])
        idx += 1
        line = file[idx]

    pages = []
    idx += 1
    while idx < len(file):
        pages.append(file[idx][0:-1])
        idx += 1

    return rules, pages


rules, pages = get_file_data("input")


def rule_check(rule, page):
    before_num = re.findall(".*\\|", rule)[0][0:-1]
    after_num = re.findall("\\|.*", rule)[0][1:]
    before_idx = page.find(before_num)
    after_idx = page.find(after_num)
    print(before_idx, after_idx)

    return before_idx < after_idx or (before_idx == -1 and after_idx == -1)


def find_middle_num(number_string):
    string_array = number_string.split(",")
    return int(string_array[len(string_array) // 2])

valid = []

for page in pages:
    safe = True
    for rule in rules:
        safe = rule_check(rule, page)

    if safe:
        valid.append(page)

total = 0

for valid_page in valid:
    total += find_middle_num(valid_page)

print(total)
