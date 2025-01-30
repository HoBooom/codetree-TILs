n = int(input())

line = [0]* (201)

segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!

for i,item in enumerate(segments):
    for j in range(item[0] + 100,item[1] + 100):
        line[j] += 1

print(max(line))