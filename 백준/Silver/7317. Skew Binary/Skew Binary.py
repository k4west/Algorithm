import sys

n = 1
li = [(n := n << 1) - 1 for _ in range(26)]
input = sys.stdin.readline
for _ in range(int(input())):
    if d := int(input()):
        s = d
        tmp, i = [], 25
        while d:
            while d >= li[i]:
                tmp.append(i)
                d -= li[i]
            i -= 1

        print(f"{s} {tmp[::-1]}".replace(", ", ","))
    else:
        print("0 []")
