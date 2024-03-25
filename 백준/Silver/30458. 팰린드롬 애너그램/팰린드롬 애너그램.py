import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    s = input().rstrip()
    d = {chr(i): 0 for i in range(97, 123)}
    if N % 2:
        d[s[N // 2]] -= 1
    for t in s:
        d[t] += 1
    for v in d.values():
        if v % 2:
            print("No")
            return
    print("Yes")
main()