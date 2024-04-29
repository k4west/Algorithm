import sys
def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    c = 0
    prev = 0
    for d in map(int, input().split()):
        if prev > d:
            c += 1
        prev = d
    print(c)
main()