def bt(i, s):
    if i == k:
        st.add(s)
        return

    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            bt(i+1, s+card[j])
            visited[j] = 0


n = int(input())
k = int(input())
card = [input() for _ in range(n)]
st = set()
visited = [0]*n
bt(0, '')
print(len(st))