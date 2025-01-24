n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

ans = 0

def f(n,ans):
    if n == 0:
        return ans
    if arr[n] > ans:
        ans = arr[n]
    return f(n-1,ans)

print(f(n-1,ans))