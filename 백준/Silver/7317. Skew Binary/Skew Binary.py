import sys
input = sys.stdin.readline
li = [(1 << i) - 1 for i in range(1, 27)]
for _ in range(int(input())):
    d = t = int(input())
    tmp = []
    for i in range(25, -1, -1):
        while t >= li[i]:
            tmp.append(i)
            t -= li[i]
    tmp = ",".join(map(str, tmp[::-1]))
    print(f"{d} [{tmp}]")