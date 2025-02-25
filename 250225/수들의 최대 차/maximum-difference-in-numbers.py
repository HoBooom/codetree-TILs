n,k = map(int,input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

ans = 0

idx1 = 0
def next_idx(idx1,idx2):
    for i in range(idx1 + 1, idx2 + 1):
        if arr[idx2] - arr[i] <= k:
            return i
    return idx2


for idx2 in range(n):
    if arr[idx2] - arr[idx1] > k:
        idx1 = next_idx(idx1,idx2)
    else:
        length = idx2 - idx1 + 1
        #print(f'length {length}, idx1 {idx1} idx2 {idx2}',end=" ")
        if length > ans:
            ans = length
        #print(arr[idx1:idx2+1])
print(ans)

