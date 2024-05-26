ee=0
eb =0

arr = input()

for i in range(len(arr)):
    if arr[i:i+2] == "ee":
        ee +=1
    if arr[i:i+2]=="eb":
        eb +=1

print(ee,eb)