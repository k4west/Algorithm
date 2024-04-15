import sys
input = sys.stdin.readline

def main():
    ans = []
    for _ in range(int(input())):
        k = int(input())
        words = [input().rstrip() for _ in range(k)]
        flag = False
        for i in range(k):
            a = words[i]
            for j in range(k):
                if i == j:
                    continue
                b = words[j]
                s = a+b
                if s == s[::-1]:
                    ans.append(s)
                    flag = True
                    break
            if flag:
                break
        if not flag:
            ans.append('0')
    print("\n".join(ans))

main()