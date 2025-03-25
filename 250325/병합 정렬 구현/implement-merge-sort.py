n = int(input())

nums = list(map(int,input().split()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr,right_arr)

def merge(left_arr,right_arr):
    temp_arr = []
    left_idx = right_idx = 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            temp_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            temp_arr.append(right_arr[right_idx])
            right_idx += 1
    
    temp_arr.extend(left_arr[left_idx:])
    temp_arr.extend(right_arr[right_idx:])

    return temp_arr

nums = merge_sort(nums)

print(*nums)
    