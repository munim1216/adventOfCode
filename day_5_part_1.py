import re


def get_file_data(file_name):
    f = open(file_name)

    file = []

    for line in f:
        file.append(line)

    rules = []
    idx = 0

    line = file[idx]
    while not line.isspace():
        print(file[idx])
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

    return before_idx < after_idx


valid = []
for page in pages:
    safe = True
    rule_number = 0
    while safe and rule_number < len(rules):
        safe = rule_check(rules[rule_number], page)
        rule_number += 1

    if safe:
        valid.append(page)

print(valid)
