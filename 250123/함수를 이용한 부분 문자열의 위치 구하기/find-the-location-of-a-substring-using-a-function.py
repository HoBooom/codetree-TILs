text = input()
pattern = input()

# Write your code here!

ans = 0

def check(i):
    for j in range(len(pattern)):
        if pattern[0 + j] != text[i + j]:
            return False
    return True
    
    

if pattern in text:
    for i in range(len(text)):
        if text[i] == pattern[0]:
            if check(i):
                ans = i
                break
else:
    ans = -1

print(ans)
                

