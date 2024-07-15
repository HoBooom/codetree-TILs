def f(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + f(n -2)
    else:
        return n + f(n - 2)

n = int(input())
print(f(n))