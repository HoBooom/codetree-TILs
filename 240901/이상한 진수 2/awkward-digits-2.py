bin_num = list(input())

int_num = 0

for i,v in enumerate(bin_num):
    if v == '0':
        bin_num[i] = '1'
        break

if '0' not in bin_num:
    bin_num[-1] = '0'

for i,v in enumerate(reversed(bin_num)):
    int_num += int(v)*(2**i)

print(int_num)