def swich_chair(men_move, men_in_chair, commend_a, commend_b, k):
    for i in range(k):
        ca = commend_a[i] #1
        cb = commend_b[i] #3
        men_A = men_in_chair[ca] #1남
        men_B = men_in_chair[cb] #3남
        men_in_chair[ca],men_in_chair[cb] = men_in_chair[cb],men_in_chair[ca]

        if cb not in men_move[men_A]:
            men_move[men_A].append(cb)
        if ca not in men_move[men_B]:
            men_move[men_B].append(ca)

    return men_move,men_in_chair 

def deepcopy(lst):
    return [item[:] for item in lst]


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


while True:
    post_move = deepcopy(men_move)
    men_move, men_in_chair = swich_chair(men_move,men_in_chair, commend_a, commend_b, k)
    
    if post_move == men_move:
        break




for i in range(n):
    print(len(men_move[i]))