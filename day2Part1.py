def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def string_to_int_list(str): ## TODO FIX THIS STUPID MEHOD FROM DAY ONE!!!!!!!!!!
    int_list = list()
    for s in str:
        print(s)
        int_list.append(int(s))
    return int_list


def check(report, idx, previous_difference):
    difference = report[idx] - report[idx + 1]
    same_sign = (difference < 0 and previous_difference < 0) or (difference > 0 and previous_difference > 0)
    if abs(difference) > 3 or difference == 0 or same_sign:
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

for data in file_data:
    print(data)
    report = string_to_int_list(data)
    if first_check(report, 0):
        safe_reports += 1


print(safe_reports)