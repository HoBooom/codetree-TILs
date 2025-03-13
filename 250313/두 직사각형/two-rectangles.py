x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

board1 = [
    [0 for _ in range(200)] for _ in range(200)
]

is_over = False

if a2 < x1 or x2 < a1:
    None
else:
    if y1 > b2 or y2 < b1:
        None
    else:
        is_over = True

if is_over:
    print("overlapping")
else:
    print("nonoverlapping")
    