n = int(input())

nums = list(map(int,input().split()))

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i + 1],arr[high] = arr[high],arr[i + 1]
    return i + 1

def quick_sort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr,low,pivot - 1)
        quick_sort(arr,pivot + 1, high)


quick_sort(nums,0,n - 1)

print(*nums)

