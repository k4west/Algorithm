def bt(s, cnt, arr):
    global ans
    
    if M-s+cnt < ans:
        return
    
    if ans < cnt:
        ans = cnt
    
    for i in range(s, M):
        r, c = arr[i]
        if not v1[r+c] and not v2[r-c]:
            v1[r+c] = v2[r-c] = 1
            bt(i+1, cnt+1, arr)
            v1[r+c] = v2[r-c] = 0


N = int(input())
w, b = [], []
for r in range(N):
    for c, k in enumerate(input().split()):
        if k == "1":
            if (r+c) % 2:
                w.append((r, c))
            else:
                b.append((r, c))

ans = 0
M = len(w)
v1, v2 = [0]*2*N, [0]*2*N
bt(0, 0, w)
ans_w = ans

ans = 0
M = len(b)
v1, v2 = [0]*2*N, [0]*2*N
bt(0, 0, b)
print(ans_w + ans)