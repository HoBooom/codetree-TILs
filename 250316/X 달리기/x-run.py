#1부터 a까지(a가 최고 속력)의 합
#다시 a - 1부터 1까지 합
#두개 합이 X이면 최소시간
#근데 X가 f(a) ~f(a + 1) 사이에 있으면
#f(a - 1)시간을 1초씩 늘려가면서 찾기
X = int(input())

max_speed = 0

for i in range(1,X + 1):
    if i ** 2 >= X:
        max_speed = i if i ** 2 == X else i - 1
        break
        

remain_dis = X - (max_speed ** 2) 
time = 2 * max_speed - 1
while remain_dis > 0:
    if remain_dis >= max_speed:
        time += 1
        remain_dis -= max_speed
    else:
        max_speed -= 1
print(time)




    
        
    