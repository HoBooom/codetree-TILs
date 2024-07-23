n = int(input())

numbers = list(map(int,input().split()))

def sub_f(a,b):
    if b == 0:
        return a
    else:
        return sub_f(b, a%b)
        
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