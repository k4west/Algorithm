import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    arr = sorted([int(input()) for _ in range(n)])
    s = sum(arr) + sum(arr[(n+1)//2:]) - sum(arr[:n//2])
    print(s)

if __name__ == "__main__":
    main()