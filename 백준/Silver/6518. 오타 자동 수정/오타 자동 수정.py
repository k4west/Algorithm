import sys

def sol(x):
    if x in dict_li: return x + li[0]
    n = len(x)
    for word in dict_li:
        m = len(word)
        if m == n + 1:
            flag, t = True, 0
            for i in range(n):
                if t == 2:
                    flag = False
                    break
                if x[i] == word[i + t]: continue
                elif i + t + 1 < m and x[i] == word[i + t + 1]: t += 1
                else:
                    flag = False
                    break
            if flag: return x + li[1] + word
        if m == n - 1:
            flag, t = True, 0
            for i in range(m):
                if t == 2:
                    flag = False
                    break
                if word[i] == x[i + t]: continue
                elif i + t + 1 < n and word[i] == x[i + t + 1]: t += 1
                else:
                    flag = False
                    break
            if flag: return x + li[1] + word
        if m == n:
            c = 0
            for i in range(n):
                if x[i] != word[i]:
                    c += 1
                    if c == 2: break
                    elif i < n - 1 and x[i] == word[i + 1] and x[i + 1] == word[i]: c -= 1
            if c < 2: return x + li[1] + word
    return x + li[2]

if __name__ == "__main__":
    input = sys.stdin.readline
    li = (" is correct", " is a misspelling of ", " is unknown")
    dict_li = [input().strip() for _ in range(int(input()))]
    for _ in range(int(input())): print(sol(input().strip()))