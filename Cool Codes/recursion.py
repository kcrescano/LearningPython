# posted
def is_sorted(n):
    if n < 10:
        return True
    ones = n % 10
    tens = n // 10 % 10
    return ones <= tens and is_sorted(n // 10)

print(is_sorted(int(input())))
#************************************************************
def sum_largest(n, k):
    if n and k:
        return int(n.pop()) + sum_largest(n, k - 1)
    return 0

number = input()
digits = int(input())

print(sum_largest(sorted(number), digits))
