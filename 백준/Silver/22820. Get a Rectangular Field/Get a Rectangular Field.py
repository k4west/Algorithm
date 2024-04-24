import sys

def main():
    n, *li = sys.stdin.readlines()
    ans = []
    for i in range(int(n)):
        maps = [list(map(int, line.rstrip().split())) for line in li[i*6:(i+1)*6]]
        m = 0
        for j in range(5):
            for k in range(5):
                for s in range(1, 6 - j):
                    for t in range(1, 6 - k):
                        if all(maps[p][q] for p in range(j, j+s) for q in range(k, k+t)):
                            if m < s*t:
                                m = s*t
        ans.append(m)
    print("\n".join(map(str, ans)))
main()