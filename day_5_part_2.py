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


rules, pages = get_file_data("tester")


def str_rule_check(rule, page):
    before_idx, after_idx = find_indexes_for_rule(rule, page)

    if before_idx == -1 or after_idx == -1:
        return True

    return before_idx < after_idx

def find_numbers_to_be_swapped(page):
    index = 0
    bad_numbers_not_found = True
    rule_to_fix = None
    while bad_numbers_not_found:
        if not str_rule_check(rules[index], page):
            bad_numbers_not_found = False
            rule_to_fix = rules[index]

    return rule_to_fix


def find_indexes_for_rule(rule, page):
    before_num = re.findall(".*\\|", rule)[0][0:-1]
    after_num = re.findall("\\|.*", rule)[0][1:]
    before_idx = page.find(before_num)
    after_idx = page.find(after_num)

    return before_idx, after_idx

def swapper(page, left_idx, right_idx):
    left_str = page[0:left_idx]
    right_str = page[left_idx+3:]
    print("LEFT:", left_str, "RIGHT:", right_str)


def find_middle_num(number_string):
    string_array = number_string.split(",")
    return int(string_array[len(string_array) // 2])


valid = []
invalid = []

for page in pages:
    safe = True
    for rule in rules:
        safe = str_rule_check(rule, page)
        if not safe:
            break

    if safe:
        valid.append(page)
    else:
        invalid.append(page)

total = 0
print(len(valid))
for valid_page in valid:
    total += find_middle_num(valid_page)

print(total)
print(invalid[0])
swapper(invalid[0], 110, 11)