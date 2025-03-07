n, k = map(int,input().split())

boom = [int(input()) for _ in range(n)]

big_boom = -1

for i in range(n):
    for j in range(i + 1, n):
        if boom[i] == boom[j] and abs(j - i) <= k:
            big_boom = max(big_boom,boom[i])

print(big_boom)

        