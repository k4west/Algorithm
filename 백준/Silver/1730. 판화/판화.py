d = {'U': (0, -1, 1), 'D': (0, 1, 1), 'L': (-1, 0, 2), 'R': (1, 0, 2)}
trace = ".|-+"      # {0: ".", 1: "|", 2: "-", 3: "+"}

N = int(input())
graph = [[0]*N for _ in range(N)]

r = c = 0
for i in input():
    dr, dc, t = d[i]
    nr = r + dr
    nc = c + dc
    
    if 0 <= nr < N and 0 <= nc < N:
        graph[c][r] |= t
        graph[nc][nr] |= t
        r, c = nr, nc
    
    # | 비트 연산(or); 피연산자 이진수 자리에 하나라도 1이면 1로 아니면 0으로 계산
    # 0 | 1 = 1 | 1 = 1 -> |
    # 0 | 2 = 2 | 2 = 2 -> -
    # 1 | 2 = 2 | 1 = 3 -> +

print('\n'.join(''.join(trace[i] for i in row) for row in graph))
