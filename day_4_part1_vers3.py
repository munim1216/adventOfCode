import re


def get_file_data(file_name):
    f = open(file_name)
    one_d_array = []
    for line in f:
        one_d_array.append(line.rstrip())
    two_d_array = []
    for line in one_d_array:
        row = []
        for letter in line:
            row.append(letter)
        two_d_array.append(row)

    return one_d_array, two_d_array


def get_col_arr(array):
    cols = []
    for c in range(len(array)):
        str_col = ""
        for r in range(len(array)):
            str_col += array[r][c]
        cols.append(str_col)

    return cols


def top_left_to_bottom_right(array, r, c, full_line):
    if r >= len(array) or c >= len(array):
        return full_line
    else:
        full_line += array[r][c]
        return top_left_to_bottom_right(array, r + 1, c + 1, full_line)


def top_left_to_bottom_right_array(grid_array):
    diag = []
    for i in range(len(grid_array)):
        diag.append(top_left_to_bottom_right(grid_array, i, 0, ""))

    i = 1
    while i < len(grid_array):
        diag.append(top_left_to_bottom_right(grid_array, 0, i, ""))
        i += 1

    return diag


def solve_direction(array):
    instances = 0
    '''for line in array:
        all_matches = re.findall("XMAS|SAMX", line, True)
        overlap_matches = re.findall("XMASAMX|SAMXMAS", line)
        instances += len(all_matches) + len(overlap_matches)
        print(line)'''
    for line in array:
        for j in range(len(array) - 4):
            if line == SOLUTION_1 or line == SOLUTION_2:
                instances += 1

    return instances


reps = 0

SOLUTION_1 = "XMAS"
print(SOLUTION_1[1:3])
SOLUTION_2 = "SAMX"

line_array, letter_array = get_file_data("hell.txt")
col_array = get_col_arr(letter_array)
#right_diagonal_array = get_right_diagonal_arr(letter_array)
#left_diagonal_array = get_left_diagonal_arr(letter_array)

reps += solve_direction(top_left_to_bottom_right_array(letter_array))

#reps = solve_direction(col_array)

'''
reps += solve_direction(line_array)
reps += solve_direction(col_array)
reps += solve_direction(right_diagonal_array)
reps += solve_direction(left_diagonal_array)
'''
print(reps)

'''
print("\n\n\nLEFT\n\n\n")
for a in left_diagonal_array:
    print(a)

print("\n\n\nRIGHT\n\n\n")

for a in right_diagonal_array:
    print(a)

print("\n\n\nCOLUMN\n\n\n")

for a in col_array:
    print(a)

print("\n\n\nROW\n\n\n")

for a in line_array:
    print(a)


print(reps)'''
