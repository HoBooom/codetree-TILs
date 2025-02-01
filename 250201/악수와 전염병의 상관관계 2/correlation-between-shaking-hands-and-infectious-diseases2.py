N, K, P, T = map(int, input().split())
#n명 개발자, k번 전염됨, p처음 걸린 개발자, t번 걸처 악수함
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Write your code here!

handshakes.sort(key = lambda x:x[0])

man = [0]*N
man[P - 1] = 1
chances = [K]*N

for _,(t,x,y) in enumerate(handshakes):
    temp = False
    if man[y-1] != 1:
        temp = True
    if man[x - 1] == 1 and chances[x - 1] > 0:
        man[y - 1] = 1
        chances[x - 1] -= 1
        if temp:
            continue
    if man[y - 1] == 1 and chances[y - 1] > 0:
        man[x - 1] = 1
        chances[y - 1] -= 1

#for _,item in enumerate(handshakes):
#    print(item)

for i,m in enumerate(man):
    print(m,end="")

    
