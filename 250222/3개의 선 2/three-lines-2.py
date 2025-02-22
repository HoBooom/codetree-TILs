n = int(input())

x_list = set()
y_list = set()

pos = []
for _ in range(n):
    x,y = map(int,input().split())
    pos.append((x,y))
    x_list.add(x)
    y_list.add(y)

x_list = list(x_list)
y_list = list(y_list)

ans = False

def check(xs,ys):
    temp = pos[:]
    for point in temp:
        if (point[0] in xs) or (point[1] in ys):
            temp[temp.index(point)] = (-1, -1)
    for point in temp:
        if point != (-1, -1):
            return False
    return True
            
        


if len(x_list) <=3 or len(y_list) <=3:
    ans = True
else:
    #x3개
    for i in range(len(x_list)):
        for j in range(i + 1,len(x_list)):
            for k in range(j + 1,len(x_list)):
                x0,x1,x2 = x_list[i],x_list[j],x_list[k]
                if check([x0,x1,x2],[]):
                    ans = True
    #y 3개
    for i in range(len(y_list)):
        for j in range(i + 1,len(y_list)):
            for k in range(j + 1,len(y_list)):
                y0,y1,y2 = y_list[i],y_list[j],y_list[k]
                if check([],[y0,y1,y2]):
                    ans = True
    #x y y
    for i in range(len(x_list)):
        for j in range(len(y_list)):
            for k in range(j+1,len(y_list)):
                x0 = x_list[i]
                y0,y1 = y_list[j],y_list[k]
                if check([x0],[y0,y1]):
                    ans = True

    #x y y
    for i in range(len(x_list)):
        for j in range(i+1,len(x_list)):
            for k in range(len(y_list)):
                x0,x1 = x_list[i],x_list[j]
                y0 = y_list[k]
                if check([x0,x1],[y0]):
                    ans = True
if ans:
    print(1)
else:
    print(0)
