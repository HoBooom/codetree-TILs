def flower(n):
    if n != 0:
        print(n,end= " ")
        flower(n - 1)
        print(n,end =" ")
    
   


n = int(input())
flower(n)