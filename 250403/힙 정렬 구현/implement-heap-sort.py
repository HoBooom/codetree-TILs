n = int(input())
nums = list(map(int,input().split()))

#이렇게 그냥 하면 왼쪽 자식은 2*i + 1 오른쪽 자식은 2*i + 2

def heapify(arr, n, cnt_idx):
    largest_n_idx = cnt_idx
    left_child_idx = cnt_idx * 2 + 1
    right_child_idx = cnt_idx * 2 + 2

    if left_child_idx < n and arr[left_child_idx] > arr[largest_n_idx]:
        largest_n_idx = left_child_idx
    elif right_child_idx < n and arr[right_child_idx] > arr[largest_n_idx]:
        largest_n_idx = right_child_idx

    if largest_n_idx != cnt_idx:
        arr[cnt_idx],arr[largest_n_idx] = arr[largest_n_idx],arr[cnt_idx]
        heapify(arr, n, cnt_idx)

def heap_sort(arr,n):
    #build_max_heap
    for i in reversed(range(n//2)):
        heapify(arr,n,i)
    #print("초기 빌드 힙",*arr)
    for i in reversed(range(n)):
        arr[0],arr[i] = arr[i],arr[0]
        #print(*arr)
        heapify(arr, i, 0)
        #print(f"{n - i}번째",*arr)

heap_sort(nums,n)
print(*nums)