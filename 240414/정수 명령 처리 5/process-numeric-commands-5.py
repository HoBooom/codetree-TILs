input_num=int(input())

arr=[]

for i in range(input_num):
    command=input()
    if "push_back" in command:
        comment,num=command.split()
        arr.append(num)
    elif "pop_back" in command:
        arr.pop()
    elif "get" in command:
        comment, num=command.split()
        print(arr[int(num)-1])
    elif "size" in command:
        print(len(arr))