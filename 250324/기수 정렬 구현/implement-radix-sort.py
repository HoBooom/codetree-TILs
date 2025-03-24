MAX_K = 6 #최대 숫자가 100000이기 때문
MAX_DIGIT = 10

n = int(input())
arr = list(map(int,input().split()))

def radix_sort():
    global arr

    p = 1
    for pos in range(MAX_K): #최대 자리수 그냥 진행
        arr_new = [[] for _ in range(MAX_DIGIT)] #숫자 임시 저장해야하니
        for elem in arr:
            digit = (elem // p) % 10
            arr_new[digit].append(elem)
        
        arr = []
        for digit in range(MAX_DIGIT):
            for elem in arr_new[digit]:
                arr.append(elem)
        p *= 10

radix_sort()

print(*arr)

