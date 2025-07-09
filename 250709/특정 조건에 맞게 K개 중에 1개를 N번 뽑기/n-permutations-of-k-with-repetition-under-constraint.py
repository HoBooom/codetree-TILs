K, N = map(int,input().split())

nums = []

def choose_n(n):
    if n == N  + 1:
        print(*nums)
        return
    
    for i in range(1, K + 1):
        if n >= 3:
            if nums[-1] == nums[-2] and nums[-1] == i:
                continue
            else:
                nums.append(i)
                choose_n(n + 1)
                nums.pop()
        else:
            nums.append(i)
            choose_n(n + 1)
            nums.pop()

choose_n(1)
            
        
