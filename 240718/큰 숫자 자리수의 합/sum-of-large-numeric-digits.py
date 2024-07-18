a,b,c = map(int,input().split())

n = a*b*c

def f(n):
    if n <= 10:
        return n % 10
    else:
        return f(n // 10) + (n % 10)

print(f(n))