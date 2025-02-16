ability = list(map(int, input().split()))

# Write your code here!

ability.sort()

team = []
ans = []

for i in range(3):
    team.append((ability[i],ability[5 - i]))
    ans.append((ability[i] + ability[5 - i]))

print(abs(max(ans) - min(ans)))


