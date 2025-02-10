a = input()
a = list(a)

ans = 0

if '0' not in a:
    a.pop()
    a.append(0)
else:
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
            #print(i,a)
            break
        #print(i,a)

#print(a)
if len(a) > 0:
    a = ''.join(a)
#print(a)
ans = int(a,2)

print(ans)