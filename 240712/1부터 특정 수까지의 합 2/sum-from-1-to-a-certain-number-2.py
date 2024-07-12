def make_sum(n):
    if n <= 1:
        return n
    else:
        return make_sum(n - 1) + n

n = int(input())

print(make_sum(n))