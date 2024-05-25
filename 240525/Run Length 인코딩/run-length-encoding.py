arr = input()
rle = []

temp = 1

for i in range(1,len(arr)):
    if arr[i] == arr[i - 1]:
        temp += 1
        if i == len(arr) - 1:
            rle.append(arr[i - 1])
            rle.append(str(temp))
    elif arr[i] != arr[i - 1]:
        rle.append(arr[i - 1])
        rle.append(str(temp))
        temp = 1


new_str = ''.join(rle)
print(len(new_str))
print(new_str)