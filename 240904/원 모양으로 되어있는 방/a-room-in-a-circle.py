import sys

INT_MAX = sys.maxsize

ans_min = INT_MAX

n= int(input())

rooms = [
    int(input()) for _ in range(n)
]

#print(rooms)

cases = []

def dis(romms,i):
    distance = 0
    start_room = i
    cnt_room = i
    temp = abs(cnt_room - start_room) - 1

    while True:
        temp += 1
        distance += rooms[cnt_room] * temp
        cnt_room = (cnt_room + 1) % n
        if cnt_room == start_room:
            break
    return distance



for i in range(n):
    ans_min = min(ans_min,dis(rooms,i))
    #print(dis(rooms,i))
print(ans_min)