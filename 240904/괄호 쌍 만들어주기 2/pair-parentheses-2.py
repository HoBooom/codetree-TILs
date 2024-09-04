command = list(input())

count = 0

count_front = 0
front_index = False

count_back = 0

for i in range(len(command) - 1):
    context = command[i]+command[i+1]
    #print(context)
    if  context == "((":
        count_front += 1
        #print(count_front,"front")
        front_index = True
    elif context == "))" and front_index == True:
        count_back += 1
       # print(count_back,"back")

print(count_front * count_back)