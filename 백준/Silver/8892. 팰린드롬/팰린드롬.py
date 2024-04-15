import sys
input = sys.stdin.readline

def check():
    k = int(input())
    words = [input().rstrip() for _ in range(k)]
    for i in range(k):
        a = words[i]
        for j in range(k):
            if i == j:
                continue
            b = words[j]
            s = a+b
            if s == s[::-1]:
                return s
    return 0

def main():
    for _ in range(int(input())):
        print(check())

main()