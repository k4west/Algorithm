import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    pattern = [input().rstrip() for _ in range(N)]
    r = sum(len([i for i in row.split('|') if i]) for row in pattern)
    c = sum(len([i for i in "".join(col).split('-') if i]) for col in zip(*pattern))
    print(r+c)

if __name__ == "__main__":
    main()