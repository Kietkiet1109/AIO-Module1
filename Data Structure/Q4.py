def word_count(file_path):
    file = open(file_path, 'r')
    word_dict = dict()

    for line in file:
        line = line.strip()
        words = line.split(' ')

        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    return word_dict


file_path = 'P1_data.txt'
print(word_count(file_path))
