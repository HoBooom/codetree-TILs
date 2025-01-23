n = int(input())

# Write your code here!

def f(n):
    if n==0:
        return

    print(n*"* ")
    f(n-1)
    print(n*"* ")

f(n)