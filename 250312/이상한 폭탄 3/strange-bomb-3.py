from collections import Counter

n, k = map(int,input().split())

boom = [int(input()) for _ in range(n)]

max_count = - 1
ans = 0

for i in range(n - k):
    cnt_boom = boom[i:i + k + 1]
    boom_counter = Counter(cnt_boom)

    for boom_number, count in boom_counter.items():
        if count >= 2 and count > max_count:
            max_count = count
            ans = boom_number
        elif count == max_count:
            ans = max(ans,boom_number)

print(ans)