D = ((-1, 0), (1, 0), (0, -1), (0, 1))
R, C, N = map(int, input().split())
maps = [input() for _ in range(R)]
if N % 2:
    if N == 1:
        print("\n".join(maps))
    else:
        for _ in range(2-(N % 4)//2):
            nxt_maps = [['O']*C for _ in range(R)]
            for r in range(R):
                for c in range(C):
                    if maps[r][c] == 'O':
                        nxt_maps[r][c] = '.'
                        for dr, dc in D:
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < R and 0 <= nc < C:
                                nxt_maps[nr][nc] = '.'
            maps = [row[:] for row in nxt_maps]
        print("\n".join("".join(row) for row in maps))

else:
    print("\n".join('O'*C for _ in range(R)))