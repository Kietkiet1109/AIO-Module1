def count_chars(inp_str):
    char_dict = dict()

    for char in inp_str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


test_string = 'Happiness'
print(count_chars(inp_str = test_string))

string = 'smiles'
print(count_chars(inp_str = string))
