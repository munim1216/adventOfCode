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


def get_right_diagonal_arr(array):
    diag = []
    for r in range(len(array)):
        diag.append(right_diag(array, r, 0, ""))

    c = len(array) - 1
    while c > 0:
        diag.append(right_diag(array, 0, c, ""))
        c -= 1

    return diag


def get_left_diagonal_arr(array):
    diag = []
    for r in range(len(array)):
        diag.append(left_diag(array, len(array) - r - 1, len(array) - 1, ""))

    c = len(array) - 2
    while c > -1:
        diag.append(left_diag(array, len(array) - 1, c, ""))
        c -= 1

    return diag


def right_diag(array, r, c, diagonal_line):
    if r < len(array) and c < len(array):
        diagonal_line += array[r][c]
        return right_diag(array, r + 1, c + 1, diagonal_line)
    else:
        return diagonal_line


def left_diag(array, r, c, diagonal_line):
    if r > -1 and c > -1:
        diagonal_line += array[r][c]
        return left_diag(array, r - 1, c - 1, diagonal_line)
    else:
        return diagonal_line


def solve_direction(array):
    print("NEXT ARRAY")
    instances = 0
    for line in array:
        all_matches = re.findall("XMAS|SAMX", line, True)
        overlap_matches = re.findall("XMASAMX|SAMXMAS", line)
        instances += len(all_matches) + len(overlap_matches)
        if all_matches.__len__() > 0:
            print(line)
    return instances


reps = 0

SOLUTION_1 = "XMAS"
SOLUTION_2 = "SAMX"

line_array, letter_array = get_file_data("hell.txt")
col_array = get_col_arr(letter_array)
right_diagonal_array = get_right_diagonal_arr(letter_array)
left_diagonal_array = get_left_diagonal_arr(letter_array)



reps += solve_direction(line_array)
reps += solve_direction(col_array)
reps += solve_direction(right_diagonal_array)
reps += solve_direction(left_diagonal_array)

print(reps)

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