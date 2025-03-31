n,m = map(int,input().split())

toast = list(input())

cnt_idx = n

def command(toast,cnt_idx,cmd, append_chr = None):
    if cmd == "L" and cnt_idx > 0:
        return toast, cnt_idx - 1
    elif cmd == "R" and cnt_idx < len(toast):
        return toast, cnt_idx + 1
    elif cmd == "D" and cnt_idx < len(toast):
        toast.pop(cnt_idx)
        return toast, cnt_idx
    elif cmd == "P":
        toast.insert(cnt_idx,append_chr)
        return toast, cnt_idx + 1
    return toast,cnt_idx

for _ in range(m):
    order = list(map(str,input().split()))
    toast,cnt_idx = command(toast, cnt_idx, order[0], order[1] if len(order) > 1 else None)
    
print(*toast,sep="")
        
        
        

