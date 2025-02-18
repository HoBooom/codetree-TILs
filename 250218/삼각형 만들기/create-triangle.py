#점 3개가 x0,y0 x0,y1, x1,y0의 좌표여야함
#즉 x좌표 2개 y좌표 2개로만 이루어져야함

n = int(input())

positions={}

for _ in range(n):
    x,y = map(int,input().split())
    if x not in positions:
        positions[x] = [y]
    else:
        positions[x].append(y)

ans = 0

def f(y_list,i):
    length = 0
    for j in range(len(y_list)):
        temp = 0
        if i == j:
            continue
        temp = abs(y_list[i] - y_list[j])
        if temp > length:
            length = temp
    return length


for key,value in positions.items():
    if len(value) >= 2:
        for i in range(len(value)):
            temp_y0 = value[i]
            temp_y1 = f(value,i)
            for key0,value0 in positions.items():
                if key0 == key:
                    continue
                if temp_y0 in value0:
                    box = abs(key - key0) * abs(temp_y1)
                    if ans < box:
                        ans = box
print(ans)



