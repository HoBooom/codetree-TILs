a, b, c = map(int, input().split())

# Write your code here!

def f(num):
    if num == 0:
        return 0
    temp = num % 10
    return f(num // 10) + temp

print(f(a*b*c))
    