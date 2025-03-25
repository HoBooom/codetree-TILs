# n = int(input())

# nums = list(map(int,input().split()))

# def partition(arr,low,high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]
    
#     arr[i + 1],arr[high] = arr[high],arr[i + 1]
#     return i + 1

# def quick_sort(arr,low,high):
#     if low < high:
#         pivot = partition(arr, low, high)

#         quick_sort(arr,low,pivot - 1)
#         quick_sort(arr,pivot + 1, high)


# quick_sort(nums,0,n - 1)

# print(*nums)

n = int(input())
nums = list(map(int,input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left_arr = [x for x in arr if x < pivot]
    middle_arr = [x for x in arr if x == pivot]
    right_arr = [x for x in arr if x > pivot]

    return quick_sort(left_arr) + middle_arr + quick_sort(right_arr)

nums = quick_sort(nums)
print(*nums)