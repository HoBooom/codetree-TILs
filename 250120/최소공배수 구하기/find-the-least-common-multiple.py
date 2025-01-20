n, m = map(int, input().split())

# Write your code here!

ans = n * m

m_cnt = 1

for i in range(1,n):
    #print(f"now {i}번째 반복, n1 {i*n}, n2 {m*m_cnt}")
    if i*n < m * m_cnt:
        #print(f"now n1 {i*n}, n2 {m*m_cnt}")
        continue
    elif i*n > m * m_cnt:
        while m * (m_cnt) < i * n:
            m_cnt += 1
            #print(f"now n1 {i*n}, n2 {m*m_cnt}")
        if i*n == m*m_cnt:
            ans = i*n
            break
    elif i*n == m*m_cnt:
        ans = i*n
        break

print(ans)
        
