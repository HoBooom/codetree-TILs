n = int(input())

lines = [list(map(int,input().split())) for _ in range(n)]

lines.sort(key = lambda x : x[1])
ans_line=[]
ans_line.append(lines[0])

count = 1

end_point = lines[0][1]

for i in range(1,n):
    start_point = lines[i][0]
    if end_point >= start_point:
        continue
    else:
        end_point = lines[i][1]
        count += 1
        ans_line.append(lines[i])

# print(lines)
# print(ans_line)
    
print(count)
