def judge_string(bracket_string):

    stack=[]

    for i in range(len(bracket_string)):
        temp=bracket_string[i]
        if temp=="(":
            stack.append(temp)
        else:
            if not stack:
                return False
            stack.pop()
    if not stack:
        return True
    return False
        

        
bracket_string=input()

answer=judge_string(bracket_string)
if answer==True:
    print("Yes")
else:
    print("No")