import sys
def f(k): 
    li = sorted(map(int, sys.stdin.readline().split()))
    print(li[-k])
if __name__ == "__main__":
    _, k = map(int, sys.stdin.readline().split())
    f(k)