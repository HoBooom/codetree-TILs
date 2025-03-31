n,m = map(int,input().split())

toast = list(input())

cnt_idx = n

def command(toast,cnt_idx,cmd, append_chr = None):
    if cmd == "L":
        if cnt_idx != 0:
            cnt_idx -= 1
    elif cmd == "R":
        if cnt_idx != n:
            cnt_idx += 1
    elif cmd == "D":
        if cnt_idx < len(toast):
            toast = toast[:cnt_idx] + toast[cnt_idx + 1:]
    elif cmd == "P":
        if cnt_idx == n:
            toast.append(append_chr)
            cnt_idx += 1
        else:
            toast = toast[:cnt_idx] + [append_chr] + toast[cnt_idx:]
            cnt_idx += 1
    return toast,cnt_idx

for _ in range(m):
    order = list(map(str,input().split()))
    if len(order) == 1:
        toast,cnt_idx = command(toast,cnt_idx,order[0])
    else:
        toast,cnt_idx = command(toast,cnt_idx,order[0],order[1])
    

print(*toast,sep="")
        
        
        

