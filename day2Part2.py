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


def check(report, idx, previous_difference):
    if idx >= len(report) - 1:
        return True
    difference = report[idx] - report[idx + 1]
    same_sign = (difference < 0 and previous_difference < 0) or (difference > 0 and previous_difference > 0)
    if abs(difference) > 3 or difference == 0 or not same_sign:
        return False
    if idx < len(report) - 1:
        return check(report, idx + 1, difference)
    return True


def first_check(report, idx):
    difference = report[idx] - report[idx + 1]
    if abs(difference) > 3 or difference == 0:
        return False
    if idx < len(report) - 1:
        return check(report, idx + 1, difference)
    return True


file_data = get_file_data("Day2Input.txt")
safe_reports = 0

line = 1

for data in file_data:
    print("Line: ", line, "Data: ", data)
    report = string_to_int_list(data.split(" "))
    safe = False
    for i in range(len(report)):
        temp_list = report.copy()
        temp_list.pop(i)
        if first_check(temp_list, 0):
            safe = True

    if safe:
        safe_reports += 1
    line += 1


print(safe_reports)
