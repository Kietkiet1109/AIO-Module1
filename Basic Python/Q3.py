import math

# Given
def is_number(n):
    try:
        float(n) # Type-casting the string to ‘float‘.
                 # If string is not a valid ‘float‘,
                 # it’ll raise ‘ValueError‘ exception
    except ValueError:
        return False
    return True


def exercise3():
    x = input('Input x = ')

    if not is_number(x):
        print('x must be a number')
        return

    x = float(x)
    activation_function = input('Input activation Function (binary|sigmoid|elu): ')

    if activation_function == 'binary':
        if x < 0:
            print('binary: f(%s) = 0' %x)
            return
        else:
            print('binary: f(%s) = 1' %x)
            return

    elif activation_function == 'sigmoid':
        print('sigmoid: f(%s) =' %x, 1 / (1 + math.e ** -x))
        return

    elif activation_function == 'elu':
        if x < 0:
            print('elu: f(%s) =' %x, 0.01 * (math.e ** x - 1))
            return
        else:
            print('elu: f(%s) =' %x, x)
            return

    else:
        print('%s is not supported' %activation_function)
        return


exercise3()
