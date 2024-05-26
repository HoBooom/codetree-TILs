a = input()

ee= False
ab = False

for i in range(len(a)):
    if a[i:i +2] =="ee":
        ee = True
    if a[i:i+2] == "ab":
        ab = True

if ee:
    print("Yes",end=" ")
else:
    print("No",end=" ")

if ab:
    print("Yes",end=" ")
else:
    print("No",end=" ")