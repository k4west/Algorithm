import sys
input = sys.stdin.readline

def palindrome(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[-i-1]:
            return False
    return s

def main():
    ans = []
    for _ in range(int(input())):
        k = int(input())
        words = [input().rstrip() for _ in range(k)]
        tmp = False
        for i in range(k-1):
            a = words[i]
            for j in range(i+1, k):
                b = words[j]
                if tmp:= palindrome(a+b) or palindrome(b+a):
                    break
            if tmp:
                ans.append(tmp)
                break
        if not tmp:
            ans.append('0')
    print("\n".join(ans))

main()