n = int(input())

list0 =[]

for i in range(n):
    temp = input()
    list0.append(temp)

alpha = input()
alpha_count = 0
len_sum = 0

for i in range(n):
    if list0[i][0] == alpha:
        alpha_count += 1
        len_sum += len(list0[i])

#mean = round(float(), 2)
mean = len_sum/alpha_count
print("{:d} {:.2f}".format(alpha_count,mean))