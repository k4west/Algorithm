import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    flag = 0
    desks, xs, ys = [0] * n, [], []
    for i in range(n):
        line = input().split()
        if "2" in line or "5" in line:
            flag += 1
        for j, d in enumerate(line):
            if flag % 2 and d == "1":
                desks[j] += 1
            if d == "2" or d == "5":
                xs.append(i)
                ys.append(j)
        if len(xs) == 2:
            break
    a, c = sorted(xs)
    b, d = sorted(ys)
    if (a - c) ** 2 + (b - d) ** 2 >= 25:
        if sum(desks[b : d + 1]) >= 3:
            print(1)
            return
    print(0)
if __name__=="__main__":
    sys.exit(main())