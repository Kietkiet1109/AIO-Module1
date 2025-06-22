def reverse_number(n):
    if n <= 0:
        return

    reverse = 0
    while n >= 10:
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = n // 10

    return reverse


print(reverse_number(n=12345678910))
print(reverse_number(n=123456789))
