a, b = map(int, input().split())

# Write your code here!

def f(a,b):
    if a > b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return a,b

a,b = f(a,b)
print(a,b)
    