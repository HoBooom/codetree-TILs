arr = input()


length = len(arr)

new = arr[:1] + 'a' + arr[2:length - 2] + 'a' +arr[length - 1:]


print(new)