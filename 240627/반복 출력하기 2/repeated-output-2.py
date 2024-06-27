def print_h(n):
    if n <1:
        return
    else:
        print("HelloWorld")
        return print_h(n-1)



n = int(input())

print_h(n)