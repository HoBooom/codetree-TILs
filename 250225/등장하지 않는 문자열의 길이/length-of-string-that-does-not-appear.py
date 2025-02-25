n = int(input())
string = list(input())

ans = n
ans_dic = {}

for i in range(n):
    temp = []
    for j in range(i,n):
        temp.append(string[j])
        length = len(temp)
        t = ''.join(temp)
        if length not in ans_dic:
            ans_dic[length] = [t]
        else:
            ans_dic[length].append(t)


for key,value in ans_dic.items():
    is_dup = False
    for i in range(len(value)):
        for j in range(i + 1,len(value)):
            if value[i] == value[j]:
                is_dup = True
    if not is_dup:
        if ans > key:
            ans = key

print(ans)
