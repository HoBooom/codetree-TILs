def quiz1(arr,index1,index2):
    temp_list = list(arr)
    temp_list[index1-1],temp_list[index2-1] = temp_list[index2-1],temp_list[index1-1]
    temp_list = ''.join(temp_list)
    return temp_list

def quiz2(arr,char1,char2):
    temp_list = list(arr)
    for i in range(len(temp_list)):
        if temp_list[i] == char1:
            temp_list[i] = char2
    temp_list = ''.join(temp_list)
    return temp_list








s, quiz = map(str,input().split())
quiz = int(quiz)

ans =[]

for i in range(quiz):
    quiz_num,a,b = map(str,input().split())
    if quiz_num == '1':
        s = quiz1(s,int(a),int(b))
        ans.append(s)
    elif quiz_num =='2':
        s = quiz2(s,a,b)
        ans.append(s)

for i in range(quiz):
    print(ans[i])