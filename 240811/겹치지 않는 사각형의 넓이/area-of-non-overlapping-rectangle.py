MAX_K = 1000

baord = [
    [ 0 for _ in range(2 * MAX_K + 1)] for _ in range(2* MAX_K + 1)
]

def make(x1,y1,x2,y2,baord,MAX_K):
    x1 += MAX_K
    y1 += MAX_K
    x2 += MAX_K
    y2 += MAX_K

    for x in range(x1,x2):
        for y in range(y1,y2):
            baord[x][y] = 1
    return baord

def erase(x1,y1,x2,y2,baord,MAX_K):
    x1 += MAX_K
    y1 += MAX_K
    x2 += MAX_K
    y2 += MAX_K

    for x in range(x1,x2):
        for y in range(y1,y2):
            baord[x][y] = 0
    return baord

count = 0

a_x1,a_y1,a_x2,a_y2 = map(int,input().split())
baord = make(a_x1,a_y1,a_x2,a_y2,baord,MAX_K)

b_x1,b_y1,b_x2,b_y2 = map(int,input().split())
baord = make(b_x1,b_y1,b_x2,b_y2,baord,MAX_K)

m_x1,m_y1,m_x2,m_y2 = map(int,input().split())
baord = erase(m_x1,m_y1,m_x2,m_y2,baord,MAX_K)

for x in range(2*MAX_K + 1):
    for y in range(2*MAX_K + 1):
        if baord[x][y] == 1:
            count += 1
print(count)