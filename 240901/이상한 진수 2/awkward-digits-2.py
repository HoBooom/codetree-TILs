bin_num = list(input())

int_num = 0
#print(bin_num)
for i,v in enumerate(bin_num):
    if v == '0':
        bin_num[i] = '1'
        break
        
#print(bin_num)

for i,v in enumerate(reversed(bin_num)):
    int_num += int(v)*(2**i)

print(int_num)