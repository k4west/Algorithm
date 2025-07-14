def counts(p, q):
    return sum(i!=j for i, j in zip(p, q))

N, M = map(int, input().split())
m = 32
pattern = ('WB'*4 + 'BW'*4) *4
board = [input() for i in range(N)]
for i in range(N-7):
    b = board[i:i+8]
    for j in range(M-7):
        count = counts(pattern, ''.join([k[j:j+8] for k in b]))
        m = min(m, count, 64-count)
print(m)