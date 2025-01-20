y = int(input())

# Write your code here!

def f(n):
    if n % 4 != 0:
        return False
    if n % 100 == 0 and n % 400 != 0:
        return False
    return True

if f(y):
    print("true")
else:
    print('false') 