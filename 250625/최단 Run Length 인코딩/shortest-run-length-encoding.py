import sys

INT_MAX = sys.maxsize

string = input()
string = (list(string))

def shift(n):
    n1 = -1 * n
    temp = string[n1:] + string[:n1]
    return check_run_len(temp)

def check_run_len(string):
    run_len = []
    cnt_n = 1
    str_len = len(string)
    for i in range(1,str_len):
        if string[i] != string[i - 1]:
            run_len.append(string[i - 1])
            run_len.append(str(cnt_n))
            cnt_n = 1
        else:
            cnt_n += 1
    run_len.append(string[-1])
    run_len.append(str(cnt_n))
    run_len = ''.join(run_len)
    #print(*string," -> ", run_len, " -> ", len(run_len))
    return len(run_len)

ans = INT_MAX

for i in range(len(string)):
    ans = min(ans,shift(i))
    #print(ans)

print(ans)
    

