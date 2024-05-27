def mul(n,m):
    return n * m

def plus(n,m):
    return n + m

def minus(n,m):
    return n - m

def div(n,m):
    ans = float(n) / float(m)
    return ans

s = input()

if '*' in s:
    n,m = map(int,s.split(" * "))
    print(f"{s} = {mul(n,m)}")
elif '/' in s:
    n,m = map(float,s.split(" / "))
    print("{} = {:.1f}".format(s,div(n,m)))
elif '+' in s:
    n,m = map(int,s.split(" + "))
    print(f"{s} = {plus(n,m)}")
elif '-' in s:
    n,m = map(int,s.split(" - "))
    print(f"{s} = {minus(n,m)}")
else:
    print(False)