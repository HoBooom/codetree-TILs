n,m = map(int,input().split())

n_list = list(map(int,input().split()))

result = 0

while m > 1:
    result += n_list[m-1]
    if m % 2 == 0:
        m = m // 2
    else:
        m -= 1
result += n_list[0]

print(result)