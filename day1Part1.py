def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def string_to_int_list(str):
    int_list = list()
    for s in str:
        int_list.append(int(s))
    return int_list


file_data = get_file_data("Day1Input.txt")
total_distance = 0

left_list = []
right_list = []

for data in file_data:
    lists = data.split("   ")
    left_list.append(int(lists[0]))
    right_list.append(int(lists[1]))

left_list.sort()
right_list.sort()

print(left_list, right_list)

for i in range(len(left_list)):
    difference = left_list[i] - right_list[i]
    difference = abs(difference)
    total_distance += difference



print(total_distance)