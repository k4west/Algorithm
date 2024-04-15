import sys

def main():
    arr = sorted(map(int, sys.stdin.readlines()[1:]))
    s = sum(arr)
    for i in range(len(arr) // 2):
        s += arr[-i-1] - arr[i]
    print(s)

if __name__ == "__main__":
    main()