n = int(input())

numbers = list(map(int,input().split()))

def sub_f(a,b):
    if a > b:
        temp = a % b
        if temp == 0:
            return b
        if b % temp == 0:
            return temp
        else:
            if b > temp:
                return sub_f(b,temp)
            else:
                return sub_f(temp,b)
    else:
        return sub_f(b,a)
        
def f(numbers,n):
    mul = numbers[n] * numbers[n - 1]
    if n == 1:
        return mul // sub_f(numbers[n],numbers[n-1])
    else:
        temp = mul // sub_f(numbers[n],numbers[n-1])
        numbers[n-1] = temp
        return f(numbers,n - 1)

print(f(numbers,n - 1))