import sys
def f(k): print(sorted(map(int, sys.stdin.readline().split()))[-k])
if __name__ == "__main__":
    _, k = map(int, sys.stdin.readline().split())
    f(k)