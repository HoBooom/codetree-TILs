import sys

INT_MAX = sys.maxsize

n,m = map(int,input().split())

lines = [
    tuple(map(int,input().split())) 
    for _ in range(m)
]

lines.sort(key = lambda x : (x[0],x[1]))
max_height = max(line[1] for line in lines)

cnt_lines = []

ans = INT_MAX


def ori_output(lines):
    ladder = [[0] * (n + 2) for _ in range(max_height + 1)]

    for a,b in lines:
        ladder[b][a] = 1

    ori_output = []
    
    for start in range(1,n + 1):
        pos = start
        for row in range(1,max_height + 1):
            if ladder[row][pos]:
                pos += 1
            elif ladder[row][pos - 1]:
                pos -= 1
        ori_output.append(pos)
    
    return ori_output

ori_output = ori_output(lines)


def line_output(cnt_lines_check):
    global ori_output

    ladder = [[0] * (n + 1) for _ in range(max_height + 1)]

    cnt_ladder_count = 0
    
    for i in range(len(cnt_lines_check)):
        if cnt_lines_check[i] == 1:
            a,b = lines[i]
            ladder[b][a] = 1
            cnt_ladder_count += 1

    output = []

    for start in range(1,n + 1):
        pos = start
        for row in range(1,max_height + 1):
            if ladder[row][pos]:
                pos += 1
            elif ladder[row][pos - 1]:
                pos -= 1
        output.append(pos)

    if output == ori_output:
        return cnt_ladder_count

    return INT_MAX

def make_ladder(num):
    global ans
    if num == m:
        cnt_output = line_output(cnt_lines)
        ans = min(ans,cnt_output)
        return 
    
    for i in range(2):
        cnt_lines.append(i)
        make_ladder(num + 1)
        cnt_lines.pop()



make_ladder(0)

print(ans)

    









