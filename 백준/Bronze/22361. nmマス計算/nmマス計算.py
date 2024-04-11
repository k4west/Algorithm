import sys
def main():
    input = sys.stdin.readline
    while True:
        n, m = map(int, input().split())
        if n == 0:
            break
        a = map(int, input().split())
        b = list(map(int, input().split()))
        c = [0] * 10
        for i in a:
            for j in b:
                k = i*j
                while k:
                    c[k%10] += 1
                    k //= 10
        print(*c, sep=' ')
main()