import sys
li = []
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    if N > 32:
        li.append('0')
        sys.stdin.readline()
        continue
    types = {}
    for mbti in sys.stdin.readline().split():
        types[mbti] = types.get(mbti, 0) + 1
    if max(types.values()) > 2:
        li.append('0')
        continue
    mbtis = []
    for mbti, n in types.items():
        mbtis.extend([mbti]*n)
    M = len(mbtis)
    s = 12
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                s = min(s, len(set(mbtis[i]) - set(mbtis[j]))+len(set(mbtis[j]) - set(mbtis[k]))+len(set(mbtis[k]) - set(mbtis[i])))
    li.append(str(s))
print("\n".join(li))