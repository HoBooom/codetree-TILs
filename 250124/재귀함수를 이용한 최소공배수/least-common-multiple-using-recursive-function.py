n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
'''
2 - 1 5 7 9 1 3
3 - 1 5 7 3 1 1
5 - 1 1 7 3 1 1
7 - 1 1 1 3 1 1
3 - 1 1 1 1 1 1
'''

def GCD(a,b):
    while b != 0:
        t = a % b
        a,b = b, t
    return abs(a)


def LCD(a,b):
    #print(f'gcd {GCD(a,b)}, lcd {a*b // GCD(a,b)}')
    return a*b // GCD(a,b)

for i in range(n - 1):
    temp = LCD(arr[i],arr[i + 1])
    arr[i + 1] = temp
    #print(arr)

print(arr[n - 1])

    