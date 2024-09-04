command = list(input())

count = 0

count_front = 0


def f(i,command):
    count_back = 0
    for j in range(i+1,len(command) - 1):
        if command[j]+command[j+1] == "))":
            count_back += 1
    return count_back

for i in range(len(command) - 1):
    context = command[i]+command[i+1]
    if context == "((":
        count += f(i,command)
    
    

print(count)