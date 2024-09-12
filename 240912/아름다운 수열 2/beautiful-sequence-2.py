n,m = map(int,input().split())

nums_a = list(map(int,input().split()))
nums_b = list(map(int,input().split()))

def is_in_list(temp_list):
    for i in range(len(temp_list)):
        if temp_list[i] not in nums_b:
            return False
    return True

count = 0

for i in range(n - m + 1):
    temp_list = nums_a[i:i + m]
    
    if is_in_list(temp_list):
        count += 1

print(count)