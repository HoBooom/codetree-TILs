N = int(input())

# Write your code here!

def f(N):
    if N==0 or N==1:
        return 1
    return f(N - 1) + f(N-2)

print(f(N-1))