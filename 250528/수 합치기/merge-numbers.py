import heapq

n = int(input())

nums = list(map(int,input().split()))
heapq.heapify(nums)

cost = 0

while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    heapq.heappush(nums,a + b)
    cost += a + b

print(cost)