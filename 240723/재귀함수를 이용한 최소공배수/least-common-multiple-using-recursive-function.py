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
        
def f(a,b):
    mul = a * b
    return (a*b) // sub_f(a,b)

def ff(numbers):
    if len(numbers) <= 1:
        return numbers.pop()
    n1 = numbers.pop()
    n2 = numbers.pop()
    numbers.append(f(n1,n2))
    return ff(numbers)

print(ff(numbers))