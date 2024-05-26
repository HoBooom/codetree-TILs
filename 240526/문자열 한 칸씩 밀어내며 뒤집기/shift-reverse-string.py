def c1(string):
    string_list = list(string)
    front = string_list.pop(0)
    string_list.append(front)
    string = ''.join(string_list)
    return string

def c2(string):
    string_list = list(string)
    back = string_list.pop()
    string_list.insert(0,back)
    string = ''.join(string_list)
    return string

def c3(string):
    string_list = list(string)
    temp_list = []
    while len(string_list) >= 1:
        temp = string_list.pop()
        temp_list.append(temp)
    string = ''.join(temp_list)
    return string

s, q = map(str,input().split())
q = int(q)

ans=[]

for _ in range(q):
    command = int(input())
    if command == 1:
        s = c1(s)
        ans.append(s)
    elif command == 2:
        s = c2(s)
        ans.append(s)
    elif command == 3:
        s = c3(s)
        ans.append(s)
    
for index,value in enumerate(ans):
    print(value)