inp = [list(input()) for _ in range(3)]

# Write your code here!

ans_set = set()

def is_win(line):
    temp = set(line)
    if len(temp) == 2:
        ans_set.add(tuple(sorted(temp)))
        return True
    return False

def check(lines):
    for line in lines:
        is_win(line)

check(inp)

check([[inp[0][c],inp[1][c],inp[2][c]]for c in range(3)])

dias = [
    [inp[0][2],inp[1][1],inp[2][0]],
    [inp[0][0],inp[1][1],inp[2][2]],
]
check(dias)

print(len(ans_set))

