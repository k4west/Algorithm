import sys

def main():
    input = sys.stdin.readline
    ans = []
    while N:=int(input()):
        tmp = [[0]*1001 for _ in range(N)]
        for i in range(N):
            input()
            for k in map(int, input().split()):
                tmp[i][k] += 1
            for k in range(1000):
                tmp[i][k+1] += tmp[i][k]
        ans.append(min(sum(abs(tmp[i][1000] - 2*tmp[i][j]) for i in range(N)) for j in range(1001)))
    print("\n".join(map(str, ans)))

main()