def get_dist(a, b):     # 맨허튼 거리
    return abs(a[0]-b[0])+abs(a[1]-b[1])


keyboard = {a: (i, j) for i, p in enumerate([zip("qwert", range(5)), zip("asdfg", range(5)), zip("zxcv", range(4)), zip(" yuiop", range(6)), zip(" hjkl", range(5)), zip("bnm", range(3))]) for a, j in p}
left = set("qwertasdfgzxcv")

total = 0
sl, sr = input().split()
lrc = keyboard[sl]
rrc = keyboard[sr]

word = input()
for s in word:
    if s in left:
        nlrc = keyboard[s]
        total += get_dist(lrc, nlrc)
        lrc = nlrc
    else:
        nrrc = keyboard[s]
        total += get_dist(rrc, nrrc)
        rrc = nrrc

print(total + len(word))    # 이동시간 + 누르는 시간
