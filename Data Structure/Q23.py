def my_function (x, y) :
    x = x + y
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]
print(my_function(list_num1, my_function(list_num2, list_num3)))

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print(my_function(list_num1, my_function(list_num2, list_num3)))
