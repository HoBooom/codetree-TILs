n = int(input())

mans = list(map(str,input().split()))

count = 0

def sort_alpha(count):
    for i in range(n - 1):
        if ord(mans[i]) > ord(mans[i + 1]):
            count += 1
            mans[i],mans[i + 1] = mans[i + 1],mans[i]
            #print(mans)
    return count

for i in range(n):
    count = sort_alpha(count)
    #print(mans)

print(count)