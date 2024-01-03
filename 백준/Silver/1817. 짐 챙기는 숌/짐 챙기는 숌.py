import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    c = t = 0

    for b in map(int, input().split()):
        t += b
        if t > M:
            t = b
            c += 1
    if t: c += 1

    print(c)

if __name__ == "__main__":
    main()