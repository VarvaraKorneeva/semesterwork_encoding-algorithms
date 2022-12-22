def coding_b_y(str_by):
    start_str = str_by
    shifts = []
    # step 1 - do shifts
    shifts.append(str_by)
    for i in range(len(str_by)-1):
        str_cut = str_by[1::]
        first_letter = str_by[0]
        str_by = str_cut + first_letter
        shifts.append(str_by)

    # step 2 - alphabetical sort
    shifts.sort()

    # step 3 - select last column
    result = ""
    for el in shifts:
        result += el[-1]

    # step 4 - find index
    number = shifts.index(start_str) + 1

    return result, number


def write_file(coding_str, str_index):
    with open("output_B_Y.txt", "w") as f:
        f.write(coding_str+"\n")
        str_index = str(str_index)
        f.write(str_index)


if __name__ == '__main__':
    string_for_B_Y = input()
    if string_for_B_Y == "":
        print("Not correct string")
        exit()
    result, number = coding_b_y(string_for_B_Y)
    write_file(result, number)
