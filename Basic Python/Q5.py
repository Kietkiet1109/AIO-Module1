def calc_pas(level):
    if level <= 0:
        return

    triangle = []
    last_row = [1]
    for i in range(level):
        if i == 0:
            triangle.append([1])
            continue

        row = [1]
        for j in range(1, i):
            row.append(last_row[j-1] + last_row[j])
        row.append(1)
        last_row = row
        triangle.append(row)

    for row in triangle:
        for value in row:
            print(value, end=' ')
        print()


def calc_fib(length):
    if length <= 0:
        return

    fib = []
    for i in range(length):
        if i == 0:
            fib.append(0)
            continue
        elif i == 1:
            fib.append(1)
            continue

        fib.append(fib[i-2] + fib[i-1])

    print('\nFibonacci sequence:')
    for value in fib:
        print(value, end=' ')


calc_pas(level=5)
calc_fib(length=9)
