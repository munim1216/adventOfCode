def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def get_answer(file_data):
    for line in file_data:
        number = int(line)

        for line2 in file_data:
            number2 = int(line2)

            if (number + number2) == 2020:
                return number * number2


file_data = get_file_data("Day1Input.txt")


# you now have a list of Strings from the input file

def string_to_int_list(str):
    int_list = list()
    for s in str:
        int_list.append(int(s))
    return int_list


total_distance = 0

for data in file_data:
    lists = data.split("   ")
    left_list = string_to_int_list(lists[0])
    right_list = string_to_int_list(lists[1])

left_list.sort()
right_list.sort()

print(left_list, right_list)

for i in range(len(left_list)):
    difference = left_list[i] - right_list[i]
    difference = abs(difference)
    total_distance += difference



print(total_distance)