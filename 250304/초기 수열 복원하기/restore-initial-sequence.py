n = int(input())

after_list = list(map(int,input().split()))

def check(num):
    ori_list = []
    ori_list.append(num)
    temp_n = 0
    cnt_n = num
    for i in range(len(after_list)):
        temp_n = after_list[i] - cnt_n
        if temp_n <= 0:
            return False
        ori_list.append(temp_n)
        cnt_n = temp_n
    #print(ori_list)
    if check_dup(ori_list):
        for i,item in enumerate(ori_list):
            print(item,end=" ")
        return True
    return False

def check_dup(ori_list):
    temp = ori_list[:]
    temp.sort()
    for i in range(1,len(temp)):
        if temp[i] == temp[i - 1]:
            return False
    return True




for i in range(1,after_list[0]):
    #print(i)
    if check(i):
        break

