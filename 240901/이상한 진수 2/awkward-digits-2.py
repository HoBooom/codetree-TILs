bin_num = list(input())

int_num = 0

def f(bin_num):
    if '0' not in bin_num:
        bin_num[-1] = '0'
    elif '0' in bin_num:
        for i,v in enumerate(bin_num):
            if v == '0':
                bin_num[i] = '1'
                break
    #print('f',bin_num)
    return bin_num

bin_num = f(bin_num)
#print(bin_num)


for i,v in enumerate(reversed(bin_num)):
    int_num += int(v)*(2**i)

print(int_num)