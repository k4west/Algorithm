def dfs(li):
    nd = {i: [] for i in map(str, range(10))}
    n = len(li)

    for last in li:
        num, length = last
        if length:
            nd[num[0]].append((num[1:], length-1))
        elif n > 1:
            return False

    for i in map(str, range(10)):
        if nd[i] and not dfs(nd[i]):
            return False
    return True


ans = []
for _ in range(int(input())):
    d = {i: [] for i in map(str, range(10))}
    for _ in range(int(input())):
        s = input()
        d[s[0]].append((s[1:], len(s)-1))

    for i in map(str, range(10)):
        if not dfs(d[i]):
            ans.append('NO')
            break
    else:
        ans.append('YES')

print('\n'.join(map(str, ans)))