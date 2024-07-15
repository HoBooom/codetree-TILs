def f(numbers,n):
    if n <= 0:
        return numbers[0]
    else:
        if numbers[n] > numbers[n-1]:
            numbers[n],numbers[n-1] = numbers[n - 1],numbers[n]
            return f(numbers,n - 1)
        else:
            return f(numbers,n - 1)



n = int(input())
numbers = list(map(int,input().split()))

print(f(numbers,n - 1))