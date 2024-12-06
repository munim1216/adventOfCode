import re


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("day3Input.txt")


def mul(x, y):
    return x * y

def get_numbers_from_string(str):
    first_number = int(re.search("[0-9]*,", str).group()[:-1])
    # first searches the inputted string for the pattern of any number then a comma. the group method returns it as a string
    # then it removes the comma by doing [:-1] which removes the last character of a string. Finally it turns it into an int
    second_number = int(re.search("[0-9]*\\)", str).group()[:-1])
    return first_number, second_number


product = 0

for data in file_data:
    matching_strs = re.findall("mul\\([0-9]*,[0-9]*\\)", data)

    for valid_data in matching_strs: # get_numbers_from_string returns 2 numbers, x and y which are multiplied togther in mul.
        x, y = get_numbers_from_string(valid_data)
        product += mul(x, y)


print(product)
