a, b = map(int, input().split())

# Write your code here!

count = 0

for i in range(a,b+1):
    if i % 2 == 0:
        continue
    if i % 10 == 5:
        continue
    if i % 3 == 0 and i % 9 != 0:
        continue
    count += 1
print(count)

