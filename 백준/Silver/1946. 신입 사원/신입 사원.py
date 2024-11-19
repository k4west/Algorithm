import sys
input = sys.stdin.readline
def main():
    t = []
    for _ in range(int(input())):
        c = 0
        n = int(input())
        m = n+1
        for _, i in sorted([tuple(map(int, input().split())) for _ in range(n)]):
            if i < m:
                c += 1
                m = i
        t.append(c)
    print('\n'.join(map(str, t)))
main()