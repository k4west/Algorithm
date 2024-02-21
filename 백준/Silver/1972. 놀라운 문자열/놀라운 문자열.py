import sys
input = sys.stdin.readline
ans = []
s = " is surprising."
ns = " is NOT surprising."
while (o:=input().strip())!="*":
    n = len(o)
    if n < 3: ans.append(o + s)
    else:
        for i in range(1, n):
            tmp = set()
            for j in range(k:=n-i): tmp.add(o[j] + o[j+i])
            if len(tmp)!=k:
                ans.append(o+ns); break
        else: ans.append(o+s)
print("\n".join(ans))