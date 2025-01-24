n = int(input())
word = [input() for _ in range(n)]

# Write your code here!

word.sort()

for i,item in enumerate(word):
    print(item)