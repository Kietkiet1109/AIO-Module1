def max_in_window(num_list, k = 3):
    max_list = list()

    for i in range(len(num_list) - k + 1):
        sliding_window = num_list[i:i+k]
        max_num = max(sliding_window)
        max_list.append(max_num)

    return max_list


test = [3, 4, 5, 1,-44]
print(max_in_window(num_list = test, k = 3))

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
print(max_in_window(num_list = num_list, k = 3))
