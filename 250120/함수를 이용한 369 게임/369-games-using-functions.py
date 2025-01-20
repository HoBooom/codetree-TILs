a, b = map(int, input().split())

# Write your code here!

def checkNum1(n):
    while n > 0:
        temp = n % 10
        if temp==3 or temp==6 or temp==9:
            return True
        n = n // 10
    
    return False

def checkNum2(n):
    if n % 3 == 0:
        return True

ans = 0

for i in range(a, b + 1):
    if checkNum1(i) or checkNum2(i):
        ans += 1

print(ans)
