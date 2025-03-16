#1부터 a까지(a가 최고 속력)의 합
#다시 a - 1부터 1까지 합
#두개 합이 X이면 최소시간
#근데 X가 f(a) ~f(a + 1) 사이에 있으면
#f(a - 1)시간을 1초씩 늘려가면서 찾기
X = int(input())

temp_high = 0

for i in range(1,X + 1):
    if i ** 2 == X:
        temp_high = i
        break
    if i ** 2 > X:
        temp_high = i - 1
        break

temp = X - (temp_high ** 2) 
time = temp_high + temp_high - 1
#print(f"befor while {time}, temp = {temp}, temp_high = {temp_high}")
while temp > 0:
    #print(temp_high, time)
    if temp >= temp_high:
        time += 1
        temp -= temp_high
    else:
        temp_high -= 1
print(time)




    
        
    