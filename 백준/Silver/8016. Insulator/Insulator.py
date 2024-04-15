import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    arr = sorted([int(input()) for _ in range(n)])
    s = sum(arr)
    for i in range(n//2):
        s += arr[-i-1] - arr[i]
    print(s)

if __name__ == "__main__":
    main()