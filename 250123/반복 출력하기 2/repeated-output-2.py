n = int(input())

# Write your code here!

def f(n):
    if n == 1:
        print("HelloWorld")
        return
    else:
        print("HelloWorld")
        return f(n - 1)

f(n)