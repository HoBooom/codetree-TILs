import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n = int(input())
a = [0] + list(map(int, input().split()))

# prefix_sum[i] : 1번째부터 i번째까지 
#                 a배열 원소의 합을 저장하고 있습니다. 
prefix_sum = [
    0
    for _ in range(n + 1)
]


# 누적합 배열에 적절한 값을 채워줍니다.
def preprocess():
    prefix_sum[1] = a[1]
    
    for i in range(2, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i]


preprocess()

# 최댓값을 구해야 하는 문제이므로
# 초기값을 INT_MIN으로 설정합니다.
ans = INT_MIN

# 모든 연속 부분수열 쌍에 대해 그들의 합 중
# 최댓값을 계산합니다.
# 이를 0 <= index1 < index2 <= n 를 만족하는 두 위치
# index1, index2를 골라 누적합의 차가 최대가 되도록 하는
# 문제로 해결이 가능하므로, 
# index2를 먼저 고정하고 index1은 index2 앞의 원소들 중
# 가장 작은 원소를 골라야 차이를 최대화 할 수 있으므로
# index2가 바뀜에따라 계속 최솟값을 O(1) 시간에 갱신하면서
# 나아갈 수 있습니다.
index1 = 0
for index2 in range(1, n + 1):
    ans = max(ans, prefix_sum[index2] - prefix_sum[index1])
    if prefix_sum[index1] > prefix_sum[index2]:
        index1 = index2

print(ans)
