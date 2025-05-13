# posted
def is_sorted(n):
    if n < 10:
        return True
    ones = n % 10
    tens = n // 10 % 10
    return ones <= tens and is_sorted(n // 10)

print(is_sorted(int(input())))
