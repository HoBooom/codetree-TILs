M, D = map(int, input().split())

# Write your code here!\

months31 = [1,3,5,7,8,10,12]
months30 = [4,6,9,11]

def f(m,d):
    if m in months31 and 1<=d<=31:
        return True
    elif m in months30 and 1<=d<=30:
        return True
    elif m == 2 and 1<=d<=28:
        return True
    else:
        return False

if f(M,D):
    print("Yes")
else:
    print("No")
