alpha = input()

list0 =[
    "apple", "banana", "grape", "blueberry", "orange"
]

count = 0

for i in range(5):
    if list0[i][2] == alpha or list0[i][3] == alpha:
        print(list0[i])
        count +=1

print(count)