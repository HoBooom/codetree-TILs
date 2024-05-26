string = input()
text= input()

len_text = len(text)
i = 0


while i < len(string):
    
    if string[i:i+len_text] == text:
        temp = string[:i] + string[i+len_text:]
        string = temp
        i = i - 2
    i += 1
    

print(string)