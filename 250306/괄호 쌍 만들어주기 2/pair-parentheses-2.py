#입력 받기
#전체 탐색
#4개탐색하면 풀림
#O^2로 푼다?

arr = input()
arr = list(arr)

count = 0

for i in range(len(arr) - 2):
    if arr[i] == '(' and arr[i + 1] == '(':
        for j in range(i + 2, len(arr) - 1):
            if arr[j] == ')' and arr[j + 1] == ')':
                count += 1

print(count)
