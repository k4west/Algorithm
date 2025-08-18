d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}  # 상하좌우
N = int(input())    # 목판의 크기 N (2 ≤ N ≤ 10)
mok = [list('.'*N) for _ in range(N)]
r = c = 0
first = True
prev = t = '.'

for dr, dc in map(lambda x: d[x], input()):     # 로봇 팔을 움직이는 명령의 순서; 최대 250
    nr, nc = r+dr, c+dc
    if 0 <= nr < N and 0 <= nc < N:             # 격자 바깥으로 나가면, 무시
        t = '|' if dr else "-"                  # 방향에 따른 흔적

        if first or (prev == t and (mok[r][c] == '.' or mok[r][c] == t)):
            mok[r][c] = t       # 첫 흔적

        else:
            mok[r][c] = '+'     # 수직, 수평

        r, c = nr, nc
        prev = t
        first = False

if mok[r][c] == '.' or mok[r][c] == t:
    mok[r][c] = t       # 첫 흔적
else:
    mok[r][c] = '+'     # 수직, 수평
print("\n".join("".join(row) for row in mok))
