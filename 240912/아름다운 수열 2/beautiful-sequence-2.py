n, m = map(int, input().split())

nums_a = list(map(int, input().split()))
nums_b = list(map(int, input().split()))

def is_in_list(temp_list, check_b):
    # check_b의 복사본을 사용하여 상태를 초기화
    temp_check_b = [v[:] for v in check_b]  # 얕은 복사 (리스트 복사)
    
    for i in range(len(temp_list)):
        if temp_list[i] not in nums_b:
            return False

        for j, v in enumerate(temp_check_b):
            if v[0] == temp_list[i] and v[1] == False:
                temp_check_b[j][1] = True
                break
        
    for v in temp_check_b:
        if v[1] == False:
            return False

    return True

count = 0

# check_b 리스트 초기화
check_b = [[nums_b[i], False] for i in range(m)]

# 슬라이딩 윈도우 방식으로 nums_a에서 부분 리스트를 추출하여 비교
for i in range(n - m + 1):
    temp_list = nums_a[i:i + m]
    
    if is_in_list(temp_list, check_b):
        count += 1

print(count)