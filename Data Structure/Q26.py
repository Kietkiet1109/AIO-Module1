def My_function (integers, number = 1) :
    result = []

    for integer in integers:
        if integer == number:
            result.append(True)
        else:
            result.append(False)

    return result


my_list = [1, 3, 9, 4]
print(My_function(my_list, -1))

my_list = [1, 2, 3, 4]
print(My_function(my_list, 2))
