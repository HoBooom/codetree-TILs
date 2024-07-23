n = int(input())

numbers = list(map(int,input().split()))

numbers.sort()

for i in numbers:
    print(i,end=" ")

print()
numbers = numbers[::-1]

for i in numbers:
    print(i,end=" ")