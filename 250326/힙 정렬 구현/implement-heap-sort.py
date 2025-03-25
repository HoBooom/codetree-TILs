n = int(input())

nums = list(map(int,input().split()))

def heapify(arr, n, cnt_idx):
    largest_idx = cnt_idx

    left_child = cnt_idx * 2 + 1
    right_child = cnt_idx * 2 + 2

    if left_child < n and arr[left_child] > arr[largest_idx]:
        largest_idx = left_child
    if right_child < n and arr[right_child] > arr[largest_idx]:
        largest_idx = right_child
    
    if largest_idx != cnt_idx:
        arr[cnt_idx],arr[largest_idx] = arr[largest_idx],arr[cnt_idx]
        heapify(arr, n, largest_idx)

def heap_sort(arr):
    for i in reversed(range(n//2 + 1)):
        heapify(arr,n,i)

    for i in reversed(range(1,n)):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr, i, 0)

heap_sort(nums)
print(*nums)
