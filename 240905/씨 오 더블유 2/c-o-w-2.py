n = int(input())

text = list(input())

count = 0

for i in range(n - 2):
    temp = 0

    if text[i] == 'C':
        for j in range(i+1,n-1):
            if text[j] == 'O':
                for k in range(j+1,n):
                    if text[k] =="W":
                        count += 1
        
print(count)