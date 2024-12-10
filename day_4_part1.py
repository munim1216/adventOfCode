def get_file_data(file_name):
    f = open(file_name)
    one_d_array = []
    for line in f:
        one_d_array.append(line.rstrip())
    two_d_array = []
    for string in one_d_array:
        two_d_array.append(list(string))

    return two_d_array


SOLUTION_1 = "XMAS"
SOLUTION_2 = "SAMX"

file_data = get_file_data("hell.txt")

print(file_data)
