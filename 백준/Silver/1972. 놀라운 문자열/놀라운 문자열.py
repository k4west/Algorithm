import sys

input = sys.stdin.readline
ans = []
surprising = " is surprising."
not_surprising = " is NOT surprising."

while (string := input().strip()) != "*":
    n = len(string)
    if n < 3:
        ans.append(string + surprising)
    else:
        for i in range(n - 1):
            tmp = set()
            for j in range(k := n - i - 1):
                tmp.add(string[j] + string[j + i + 1])
            if len(tmp) != k:
                ans.append(string + not_surprising)
                break
        else:
            ans.append(string + surprising)
print("\n".join(ans))