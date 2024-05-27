def find_index(s,obj):

    for i in range(len(s)):
        if s[i] == obj[0]:
            tf = is_in(s,obj,i)
            if tf:
                return i
    return -1

def is_in(s,obj,index):
    for i in range(len(obj)):
        if obj[i] != s[index + i]:
            return False
    return True
    
s = input()
obj = input()

ans = find_index(s,obj)
print(ans)