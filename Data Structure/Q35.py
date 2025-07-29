def my_function (x):
    result = ''

    for i in range(len(x)):
        result += x[len(x)- i - 1]

    return result


x = 'I can do it'
print(my_function(x))

x = 'apricot'
print(my_function(x))
