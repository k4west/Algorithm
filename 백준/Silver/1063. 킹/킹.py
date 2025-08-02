d = {
  'R' : (1, 0),
  'L' : (-1, 0),
  'B' : (0, -1),
  'T' : (0, 1),
  'RT' : (1, 1),
  'LT' : (-1, 1),
  'RB' : (1, -1),
  'LB' : (-1, -1)
}

king, stone, N = input().split()
kc, kr = [ord(king[0])-64, int(king[1])]
sc, sr = [ord(stone[0])-64, int(stone[1])]

for _ in range(int(N)):
    dc, dr = d[input()]
    if 0 < (nr := kr+dr) <= 8 and 0 < (nc := kc+dc) <= 8:  # 범위 안
        if nr == sr and nc == sc:
            if 0 < (nsr := sr+dr) <= 8 and 0 < (nsc := sc+dc) <= 8:
                kr, kc, sr, sc = nr, nc, nsr, nsc
        else:
            kr, kc = nr, nc

print(chr(kc+64)+str(kr))
print(chr(sc+64)+str(sr))