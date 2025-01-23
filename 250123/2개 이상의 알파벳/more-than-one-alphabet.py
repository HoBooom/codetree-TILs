A = input()

# Write your code here!

temp = []

tempList = list(A)

for idx,item in enumerate(tempList):
    if item not in temp:
        temp.append(item)

if len(temp) >= 2:
    print("Yes")
else:
    print("No")