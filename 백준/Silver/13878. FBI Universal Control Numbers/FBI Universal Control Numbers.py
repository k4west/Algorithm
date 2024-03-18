import sys
input = sys.stdin.readline
ds = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 8, 'C': 11, 'D': 12, 'E': 13, 'F': 14, 'G': 11, 'H': 15, 'I': 1, 'J': 16, 'K': 17, 'L': 18, 'M': 19, 'N': 20, 'O': 0, 'P': 21, 'Q': 0, 'R': 22, 'S': 5, 'T': 23, 'U': 24, 'V': 24, 'W': 25, 'X': 26, 'Y': 24, 'Z': 2}
ans = []
for _ in range(int(input())):
    i, m = input().split()
    dd = [ds[d] for d in m]
    if (2*dd[0]+4*dd[1]+5*dd[2]+7*dd[3]+8*dd[4]+10*dd[5]+11*dd[6]+13*dd[7])%27==dd[8]:
        s = sum(d*(27**(7-i)) for i, d in enumerate(dd[:-1]))
        ans.append(f"{i} {s}")
    else: ans.append(f"{i} Invalid")
print("\n".join(ans))