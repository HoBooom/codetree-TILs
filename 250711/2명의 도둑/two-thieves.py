n, m, c = map(int,input().split()) #n : 방 크기, m : 열 길이, c : 최대 무게

room = [
    list(map(int,input().split()))
    for _ in range(n)
]

a = []

max_val = 0

def possible_weigh(w):
    return w <= c

def is_intersect(c1,c2):
    if (c1 <= c2 <= c1 + m - 1) or (c2 <= c1 <= c2 + m - 1):
        return True
    return False

def possible_position(r1,c1,r2,c2):
    if c1 + m - 1 >= n or c2 + m - 1 >= n:
        return False
    if r1 != r2 and r1 < n and r2 < n:
        return True

    if r1 == r2 and is_intersect(c1,c2):
        return False
    
    return True

def find_max_sum(curr_idx, curr_weight, curr_val):
    global max_val
    
    if curr_idx == m:
        if curr_weight <= c:
            max_val = max(max_val, curr_val)
        return
    
    find_max_sum(curr_idx + 1,curr_weight, curr_val)
    find_max_sum(curr_idx + 1, curr_weight + a[curr_idx], curr_val + a[curr_idx] * a[curr_idx])

def find_max(r,c):
    global a,max_val

    a = room[r][c:c + m]
    
    max_val = 0
    find_max_sum(0,0,0)
    return max_val

ans = max([
    find_max(r1,c1) + find_max(r2,c2)
    for r1 in range(n)
    for c1 in range(n)
    for r2 in range(n)
    for c2 in range(n)
    if possible_position(r1,c1,r2,c2)
])

print(ans)