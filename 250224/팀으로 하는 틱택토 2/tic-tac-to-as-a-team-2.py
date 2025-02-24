inp = [list(input()) for _ in range(3)]

# Write your code here!
def is_range(r,c):
    if 0<=r<3 and 0<=c<3:
        return True
    return False

def is_win(lis):
    temp = set()
    for _,item in enumerate(lis):
        temp.add(item)
    if len(temp) == 2:
        return True
    return False

ans = 0

for r in range(3):
    if is_win(inp[r]):
        ans += 1

for c in range(3):
    temp = [inp[0][c],inp[1][c],inp[2][c]]
    if is_win(temp):
        ans += 1

temp = []
for i in range(3):
    temp.append(inp[i][i])
if is_win(temp):
    ans +=1

temp1 = [inp[0][2],inp[1][1],inp[2][0]]
if is_win(temp1):
    ans +=1 
print(ans)