class T:
    def __init__(self,c,m,t):
        self.c = c
        self.m = m
        self.t = t

c,m,t = map(str,input().split())

t = T(c,m,t)
print("secret code :",t.c)
print("meeting point :",t.m)
print("time :",t.t)