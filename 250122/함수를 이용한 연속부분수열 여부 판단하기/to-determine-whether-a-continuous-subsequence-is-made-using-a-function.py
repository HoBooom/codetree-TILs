n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Write your code here!

temp = False

for i in range(n1 - n2):
    if a[i] == b[0]:
        temp = True
        for j in range(n2):
            if b[j] != a[i + j]:
                temp = False

if temp:
    print("Yes")
else:
    print("No")