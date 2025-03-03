n,k = map(int,input().split())
arr = list(map(int,input().split()))

arr_min = min(arr)
arr_max = max(arr)

ans = arr_max

def f(temp_ans):
    idx_arr = []
    idx_arr.append(0)
    for idx,item in enumerate(arr):
        if idx == 0 or idx == (len(arr) - 1):
            if item > temp_ans:
                return False
            continue
        if item <= temp_ans:
            idx_arr.append(idx)
            #print(f"[{idx}] : {item}")
        
    if len(arr) > 1:
        idx_arr.append(len(arr) - 1)

    # print(idx_arr)
    for i in range(1,len(idx_arr)):
        if idx_arr[i] - idx_arr[i - 1] > k:
            #print('False')
            return False
    #print('True')
    return True




for i in range(arr_min,arr_max + 1):
    temp_ans = i
    #print("temp_ans ",temp_ans)
    if f(temp_ans):
        ans = min(ans,temp_ans)

print(ans)
    