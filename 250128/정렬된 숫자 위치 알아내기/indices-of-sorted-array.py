n = int(input())
sequence = list(map(int, input().split()))

# Write your code here!
seq1 = []
seq0 = []

for i,item in enumerate(sequence):
    seq1.append((item,i + 1))
    seq0.append((item,i + 1))

seq1.sort(key = lambda x:x[0])



for i,item in enumerate(seq0):
    for key,value in enumerate(seq1):
        if item == value:
            print(key + 1,end = " ")
            break