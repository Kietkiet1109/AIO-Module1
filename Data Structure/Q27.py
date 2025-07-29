def my_function (list_nums = [0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i

    return var/len(list_nums)


print(my_function([4, 6, 8]))
print(my_function())
