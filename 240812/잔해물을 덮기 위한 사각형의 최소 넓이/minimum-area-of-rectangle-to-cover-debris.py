MAX_K = 1000

board = [
    [0 for _ in range(2*MAX_K + 1)] for _ in range(2*MAX_K + 1)
]


x1,y1,x2,y2 = map(int,input().split())
x1 += MAX_K
x2 += MAX_K
y1 += MAX_K
y2 += MAX_K
for x in range(x1,x2):
    for y in range(y1,y2):
        board[x][y] = 1

a1,b1,a2,b2 = map(int,input().split())
a1 += MAX_K
a2 += MAX_K
b1 += MAX_K
b2 += MAX_K
for a in range(a1,a2):
    for b in range(b1,b2):
        board[a][b] = 0



small_x = {
    "x" : 2001,
    "small_y" : 2001,
    "big_y" : -1
}
big_x = {
    "x" : -1,
    "small_y" : 2001,
    "big_y" : -1
}

for x0 in range(2 * MAX_K + 1):
    for y0 in range(2 * MAX_K + 1):
        if board[x0][y0] == 1:
            if x0 < small_x["x"]:
                small_x["x"] = x0
            if x0 > big_x["x"]:
                big_x["x"] = x0

            if x0 == small_x["x"] and y0 < small_x["small_y"]:
                small_x["small_y"] = y0
            elif x0 == small_x["x"] and y0 > small_x["big_y"]:
                small_x["big_y"] = y0
            
            if x0 == big_x["x"] and y0 < big_x["small_y"]:
                big_x["small_y"] = y0
            elif x0 == big_x["x"] and y0 > big_x["big_y"]:
                big_x["big_y"] = y0

x_len = 0
y_len = 0

if (small_x["big_y"] - small_x["small_y"]) > (big_x["big_y"] - big_x["small_y"]):
    y_len = small_x["big_y"] - small_x["small_y"]
elif (small_x["big_y"] - small_x["small_y"]) < (big_x["big_y"] - big_x["small_y"]):
    y_len = (big_x["big_y"] - big_x["small_y"])
elif (small_x["big_y"] - small_x["small_y"]) == (big_x["big_y"] - big_x["small_y"]):
    if small_x["big_y"] - small_x["small_y"] == 0:
        y_len = 0
    else:
        y_len = small_x["big_y"] - small_x["small_y"]

if big_x["x"] - small_x["x"] == 0:
    x_len = 0
else:
    x_len = big_x["x"] - small_x["x"]

x_len += 1
y_len += 1

print(x_len * y_len)