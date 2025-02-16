N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Write your code here!


def find_nums(a1):
    n1 = set()
    for i in range(1,N + 1):
        if a1 - 2<= i <= a1 + 2:
            n1.add(i)
    if a1 == 1:
        n1.add(N)
        if N >= 2:
            n1.add(N - 1)
    if a1 == 2:
        n1.add(N)
    if a1 == N:
        n1.add(1)
        if N >= 2:
            n1.add(2)
    if a1 == N - 1:
        n1.add(1)
    return n1


def find_set(a1,b1,c1):
    n1 = find_nums(a1)
    n2 = find_nums(b1)
    n3 = find_nums(c1)
    #print(n1,n2,n3)
    sets = set()
    for i in n1:
        for j in n2:
            for k in n3:
                sets.add((i,j,k))
    return sets

ans_list1 = find_set(a1,b1,c1)
ans_list2 = find_set(a2,b2,c2)
ans_list = ans_list1 | ans_list2

print(len(ans_list))

    
    
    
