n = int(input())

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            # 첫 번째 조건: 두 좌표의 차이가 2 이하인 경우
            if (abs(a1 - i) <= 2 and abs(b1 - j) <= 2 and abs(c1 - k) <= 2) or \
               (abs(a2 - i) <= 2 and abs(b2 - j) <= 2 and abs(c2 - k) <= 2):
                count += 1
            # 두 번째 조건: 좌표계를 순환하는 경우
            elif (min((a1 - i) % n, (i - a1) % n) <= 2 and
                  min((b1 - j) % n, (j - b1) % n) <= 2 and
                  min((c1 - k) % n, (k - c1) % n) <= 2) or \
                 (min((a2 - i) % n, (i - a2) % n) <= 2 and
                  min((b2 - j) % n, (j - b2) % n) <= 2 and
                  min((c2 - k) % n, (k - c2) % n) <= 2):
                count += 1

print(count)