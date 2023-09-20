import sys 
if __name__ == "__main__":
    _, k = map(int, sys.stdin.readline().split())
    li = sorted(map(int, sys.stdin.readline().split()))
    print(li[-k])