from sys import stdin
input = stdin.readline

def main():
    N, M = map(int, input().split())
    li = list(map(int, input().split()))

    s = c = j = 0
    for i in range(N):
        s += li[i]
        while s > M:
            s -= li[j]
            j += 1
        if s == M:
            c += 1
    print(c)
        
if __name__ == "__main__":
    main()