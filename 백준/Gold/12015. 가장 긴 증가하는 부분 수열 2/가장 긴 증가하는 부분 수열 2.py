N = int(input())
*li, = map(int, input().split())
ans = [li[0]]

M = 1
for a in li[1:]:
    if ans[-1] < a:
        ans.append(a)
        M += 1
    else:
        s, e = 0, M-1
        while s <= e:
            m = (s+e)//2
            if ans[m] < a:
                s = m + 1
            else:
                e = m - 1
        if e+1 < M:
            ans[e+1] = a

print(len(ans))