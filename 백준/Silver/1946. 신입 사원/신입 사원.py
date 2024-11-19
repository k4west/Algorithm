import sys
input = sys.stdin.readline
def main():
    t = []
    for _ in range(int(input())):
        c = 1
        n = int(input())
        li = [0] * (n+1)
        for _ in range(n):
            i, j = map(int, input().split())
            li[i] = j
        m = li[1]
        for i in range(2, n+1):
            if m > (j:=li[i]):
                c += 1
                m = j
        t.append(c)
    print('\n'.join(map(str, t)))
main()