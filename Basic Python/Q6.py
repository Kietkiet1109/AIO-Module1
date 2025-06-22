def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def approx_sin(x, n):
    if n < 0:
        return

    total = 0
    for i in range(n):
        total += (-1)**i * x**(2*i + 1)/factorial(2*i + 1)
    return total


def approx_cos(x, n):
    if n < 0:
        return

    total = 0
    for i in range(n):
        total += (-1)**i * x**(2*i)/factorial(2*i)
    return total


def approx_sinh(x, n):
    if n < 0:
        return

    total = 0
    for i in range(n):
        total += x**(2*i + 1)/factorial(2*i + 1)
    return total


def approx_cosh(x, n):
    if n < 0:
        return

    total = 0
    for i in range(n):
        total += x**(2*i)/factorial(2*i)
    return total


print(approx_sin(x=3.14, n=10))
print(approx_cos(x=3.14, n=10))
print(approx_sinh(x=3.14, n=10))
print(approx_cosh(x=3.14, n=10))
