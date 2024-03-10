import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    balloon = list(range(2, n+1))
    note = list(map(int, input().split()))
    ans = [1]
    index = 0

    for i in range(1, n):
        t = note[ans[-1]-1]
        if t > 0:
            t -= 1
        index = (index + t) % (n-i)
        ans.append(balloon.pop(index))
    ans += balloon
    print(" ".join(map(str, ans)))
main()