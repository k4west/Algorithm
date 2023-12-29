import sys
input = sys.stdin.readline

def main():
    N = int(input())
    deliciousness = list(map(int, input().split()))
    s = 0
    for a in deliciousness[:-1]:
        s += a
        if s <= 0:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()