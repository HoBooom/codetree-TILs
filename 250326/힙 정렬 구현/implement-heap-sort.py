n = int(input())

nums = [0] + list(map(int,input().split()))

def heapify(arr, n, cnt_idx):
    largest_idx = cnt_idx

    left_child = cnt_idx * 2
    right_child = cnt_idx * 2 + 1

    if left_child < n and arr[left_child] > arr[largest_idx]:
        largest_idx = left_child
    if right_child < n and arr[right_child] > arr[largest_idx]:
        largest_idx = right_child
    
    if largest_idx != cnt_idx:
        arr[cnt_idx],arr[largest_idx] = arr[largest_idx],arr[cnt_idx]
        heapify(arr, n, largest_idx)

def heap_sort(arr):
    for i in reversed(range(1,n//2 + 1)):
        heapify(arr,n,i)

    for i in reversed(range(2,n)):
        arr[1],arr[i] = arr[i],arr[1]
        heapify(arr, i - 1, 1)

heap_sort(nums)
nums.pop(0)
print(*nums)
