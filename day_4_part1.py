import re


def get_file_data(file_name):
    f = open(file_name)
    one_d_array = []
    for line in f:
        one_d_array.append(line.rstrip())
    two_d_array = []
    for string in one_d_array:
        two_d_array.append(list(string))

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
    for c in range(len(array)):
        diag.append(right_diag(array, 1, c, ""))

    return diag


def get_left_diagonal_arr(array):
    diag = []
    for r in range(len(array)):
        diag.append(left_diag(array, len(array) - r - 1, len(array) - 1, ""))
    for c in range(len(array)):
        diag.append(left_diag(array, len(array) - 2, len(array) - c - 1, ""))
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


SOLUTION_1 = "XMAS"
SOLUTION_2 = "SAMX"

line_array, letter_array = get_file_data("hell.txt")
col_array = get_col_arr(letter_array)
right_diagonal_array = get_right_diagonal_arr(letter_array)
left_diagonal_array = get_left_diagonal_arr(letter_array)

reps = 0


line_arr_char_count = ""

for line in line_array:
    all_matches = re.findall("XMAS|SAMX", line)
    line_arr_char_count += line
    reps += len(all_matches)

print("Line arr: ", len(line_arr_char_count))

col_arr_char_count = ""

for line in col_array:
    all_matches = re.findall("XMAS|SAMX", line)
    col_arr_char_count += line
    reps += len(all_matches)

print("Col arr: ", len(col_arr_char_count))

right_char = ""

for line in right_diagonal_array:
    all_matches = re.findall("XMAS|SAMX", line)
    right_char += line
    reps += len(all_matches)

print("Right: ", len(right_char))

left_char = ""

for line in left_diagonal_array:
    all_matches = re.findall("XMAS|SAMX", line)
    left_char += line
    reps += len(all_matches)

print("Left: ", len(left_char))
