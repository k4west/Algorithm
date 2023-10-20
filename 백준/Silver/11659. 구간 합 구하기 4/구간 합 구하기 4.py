import sys
input = sys.stdin.readline
def main():
    N, M = map(int, input().split())
    t = [0] + list(map(int, input().split()))
    for i in range(1, N+1):
        t[i] += t[i-1]
    for _ in range(M):
        s, e = map(int, input().split())
        print(t[e]-t[s-1])
if __name__ == "__main__":
    main()