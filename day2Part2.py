def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def string_to_int_list(str): ## TODO FIX THIS STUPID MEHOD FROM DAY ONE!!!!!!!!!!
    int_list = list()
    for s in str:
        int_list.append(int(s))
    return int_list


def check(report, idx, previous_difference, mistakes):
    if idx >= len(report) - 1:
        return True

    if mistakes > 1:
        return False

    difference = report[idx] - report[idx + 1]
    same_sign = (difference < 0 and previous_difference < 0) or (difference > 0 and previous_difference > 0)
    if abs(difference) > 3 or difference == 0 or not same_sign:
        mistakes += 1
        report.pop(idx)
        return check(report, idx, previous_difference, mistakes)
    if idx < len(report) - 1:
        return check(report, idx + 1, difference, mistakes)
    return True


def first_check(report, idx):
    difference = report[idx] - report[idx + 1]
    mistakes = 0
    if abs(difference) > 3 or difference == 0:
        mistakes += 1
    if idx < len(report) - 1:
        return check(report, idx + 1, difference, mistakes)
    return True


file_data = get_file_data("Day2Input.txt")
safe_reports = 0

line = 1

for data in file_data:
    print("Line: ", line, "Data: ", data)
    report = string_to_int_list(data.split(" "))
    if first_check(report, 0):
        safe_reports += 1
    line += 1


print(safe_reports)
