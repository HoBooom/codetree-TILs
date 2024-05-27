def swich_chair(men_move, men_in_chair, commend_a, commend_b, k):
    for i in range(k):
        ca = commend_a[i] #1
        cb = commend_b[i] #3
        men_A = men_in_chair[ca] #1남
        men_b = men_in_chair[cb] #3남
        men_in_chair[ca],men_in_chair[cb] = men_in_chair[cb],men_in_chair[ca]

        if cb not in men_move[men_A]:
            men_move[men_A].append(cb)
        if ca not in men_move[men_b]:
            men_move[men_b].append(ca)

    return men_move,men_in_chair  


n,k = map(int,input().split())

men_in_chair = [i for i in range(n)]



commend_a = []
commend_b = []

for i in range(k):
    a,b = map(int,input().split())
    commend_a.append(a - 1)
    commend_b.append(b - 1)
   

men_move =[
    [] for _ in range(n)
]

for i in range(n):
    men_move[i].append(i)


for i in range(3):
    men_move, men_in_chair = swich_chair(men_move,men_in_chair, commend_a, commend_b, k)



for i in range(n):
    print(len(men_move[i]))