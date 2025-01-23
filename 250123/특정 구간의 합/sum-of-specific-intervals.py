n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!

arr.insert(0,0)

for i,items in enumerate(queries):
    print(sum(arr[items[0]:items[1] + 1]))