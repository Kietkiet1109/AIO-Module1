def function_helper (x, data):
    for i in data:
        if i == x:
            return 0

    return 1


def my_function (data):
    res = []

    for i in data:
        if function_helper(i, res):
            res.append (i)

    return res


lst = [10, 10, 9, 7, 7]
print(my_function(lst))

lst = [9, 9, 8, 1, 1]
print(my_function(lst))
