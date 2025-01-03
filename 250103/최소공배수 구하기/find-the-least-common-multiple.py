n,m = map(int,input().split())

def q(n,m):
    n0 = n
    m0 = m
    n1 = 1
    n2 = 1
    while True:
        if n == m:
            return n
        elif n > m:
            n2 += 1
            m = m0 * n2
        elif n < m:
            n1 += 1
            n = n0 * n1
    return -1

print(q(n,m))
        