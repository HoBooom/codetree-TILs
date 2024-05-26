arr,alpha = map(str,input().split())

place = -1

for i in range(len(arr)):
    if arr[i] == alpha:
        place = i
    
if place == -1:
    print("No")
else:
    print(place)