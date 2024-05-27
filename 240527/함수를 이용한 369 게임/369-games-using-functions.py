def is_369(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] == '3'or n[i]=='6' or n[i]=='9':
            return True
    return False

def is_mul_3(n):
    if n % 3 ==0:
        return True
    return False

n,m = map(int,input().split())

count = 0 

for i in range(n, m + 1):
    if is_369(i) or is_mul_3(i):
        count += 1

print(count)