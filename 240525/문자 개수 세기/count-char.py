a = input()
alpha = input()

count = 0

for i in range(len(a)):
    if a[i] == alpha:
        count +=1

print(count)