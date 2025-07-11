import sys

INT_MIN = -sys.maxsize

input_oper = list(input())

nums = {}

ans = INT_MIN

opers = []

for i in range(len(input_oper)):
    if input_oper[i] == "*" or input_oper[i] == "+" or input_oper[i] == "-":
        opers.append(input_oper)
    else:
        nums[f"{input_oper[i]}"] = 0

len_nums = len(nums)
nums_list = []

def get_num(nums_list):
    idx = 0
    for key, _ in nums.items():
        nums[key] = nums_list[idx]
        idx += 1

    output = nums[input_oper[0]]

    for i in range(1,len(input_oper)):
        if input_oper[i-1] == "+":
            output += nums[input_oper[i]]
        elif input_oper[i-1] == "-":
            output -= nums[input_oper[i]]
        elif input_oper[i-1] == "*":
            output *= nums[input_oper[i]]
    
    return output


def set_nums(n):
    global ans
    if n == len_nums:
        oper_n = get_num(nums_list)
        ans = max(ans, oper_n)
        return 
    
    for i in range(1,4 + 1):
        nums_list.append(i)
        set_nums(n + 1)
        nums_list.pop()

set_nums(0)

print(ans)





