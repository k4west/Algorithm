def bt(i, n, s):
    if n == 6:
        tmp.append(s.lstrip())
        return
    
    bt(i+1, n+1, f"{s} {S[i]}")
    if k-i > 6-n:
        bt(i+1, n, s)

ans = []
while True:
    k, *S = map(int, input().split())
    if not k:
        break
    
    tmp = []
    bt(0, 0, "")
    ans.append("\n".join(tmp))
print("\n\n".join(ans))