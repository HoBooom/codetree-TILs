n = int(input())
date = []
day = []
weather = []
datas = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
    year,month,datee = map(int,d.split('-'))
    datas.append([year,month,datee,dy,w])

# Write your code here!

datas.sort(key = lambda x:(x[0],x[1],x[2]))

def first_rain(datas):
    for i,items in enumerate(datas):
        if items[1]<10:
            items[1] = '0'+str(items[1])
        if items[2]<10:
            items[2] = '0'+str(items[2])   
        if items[4] == 'Rain':
            print(f"{items[0]}-{items[1]}-{items[2]} {items[3]} {items[4]}")
            return
    return

first_rain(datas)