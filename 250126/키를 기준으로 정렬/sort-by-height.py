n = int(input())
name = []
height = []
weight = []

peoples = []

class People:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def printData(self):
        print(f"{self.name} {self.height} {self.weight}")

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))
    man = People(n_i,int(h_i),int(w_i))
    peoples.append(man)

peoples.sort(key = lambda x:x.height)


# Write your code here! 



for i,item in enumerate(peoples):
    item.printData()


