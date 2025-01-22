Y, M, D = map(int, input().split())

# Write your code here!

def checkYear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False

months31=[1,3,5,7,8,10,12]
months30=[4,6,9,11]

def checkSeason(m):
    if 3<=m<=5:
        print("Spring")
    elif 6<=m<=8:
        print("Summer")
    elif 9<=m<=11:
        print("Fall")
    elif m == 12 or 1<=m<=2:
        print("Winter")
    else:
        print(-1)


if checkYear(Y): #윤년이면
    if M == 2 and 1<=D<=29:
        print("Winter")
    elif M in months30 and 1<=D<=30:
        checkSeason(M)
    elif M in months31 and 1<=D<=31:
        checkSeason(M)
    else:
        print(-1)
else: #윤년이 아니면
    if M == 2 and 1<=D<=28:
        print("Winter")
    elif M in months30 and 1<=D<=30:
        checkSeason(M)
    elif M in months31 and 1<=D<=31:
        checkSeason(M)
    else:
        print(-1)

        