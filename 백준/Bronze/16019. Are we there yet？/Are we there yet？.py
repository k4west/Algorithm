arr = list(map(int, input().split()))
ans = []
for i in range(5):
    tmp = [0] * 5
    s = t = 0
    for j in range(i, i+4):
        if j < 4:
            s += arr[j]
            tmp[j+1] = s
        else:
            t += arr[i-j%4-1]
            tmp[i-j%4-1] = t
    ans.append(' '.join(map(str, tmp)))
print(*ans, sep='\n')