from algorithm_B_Y import coding_b_y


def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
        if not data:
            print("Not correct alphabet")
            exit()
        if data[-1] == "\n":
            data = data[:-1:]
        data = data.split(" ")

    return data


def coding_stack_of_books(alph_list, str_sob):
    alph = {}
    # add index
    for i in range(len(alph_list)):
        alph[i] = alph_list[i]

    result = ""
    index = 0
    for el in str_sob:
        # find code for symbol
        for k, v in alph.items():
            if v == el:
                result += str(k)
                index = k
        # move to top
        ind_val = alph[index]
        for i in range(index):
            alph[index-i] = alph[index-i-1]
        alph[0] = ind_val

    return result


def write_file(coding_str, number_by):
    with open("output_sob.txt", "w") as f:
        f.write(coding_str+"\n")
        number_by = str(number_by)
        f.write(number_by)


if __name__ == '__main__':
    alphabet = read_file("alphabet_for_sob.txt")
    string_for_sob = input()
    if string_for_sob == "":
        print("Not correct string")
        exit()
    correct = True
    for el in string_for_sob:
        if el not in alphabet:
            print(f"The character '{el}' is not in the alphabet")
            correct = False
    if not correct:
        exit()
    result = coding_stack_of_books(alphabet, string_for_sob)
    _, number = coding_b_y(string_for_sob)
    write_file(result, number)
