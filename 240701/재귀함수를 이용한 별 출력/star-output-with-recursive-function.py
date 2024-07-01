def make_star(n):
    if n == 0:
        return
    make_star(n - 1) 
    print('*'*n)


n = int(input())

make_star(n)