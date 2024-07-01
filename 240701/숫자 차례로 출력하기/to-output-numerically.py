def to_n(n,i):
    if i == n:
        print(i)
        return
    else:
        print(i,end=" ")
        return to_n(n,i+1)

def to_1(n):
    if n == 1:
        print(n)
    else:
        print(n,end=" ")
        return to_1(n - 1)

n = int(input())

to_n(n,1)
to_1(n)