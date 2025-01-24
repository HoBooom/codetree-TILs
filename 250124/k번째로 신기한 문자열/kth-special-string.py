n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Write your code here!

temp = []

def check(t,str):
    for i in range(len(t)):
        if str[i] != t[i]:
            return False
    return True

for i,item in enumerate(str):
    if check(t,item):
        temp.append(item)

temp.sort()

print(temp[k-1])