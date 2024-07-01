def starline(n):
    if n != 0:
        print('* '*n)
        starline(n - 1)
        print("* "*n)

n = int(input())

starline(n)