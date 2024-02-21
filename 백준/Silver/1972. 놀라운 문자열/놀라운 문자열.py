import sys
def sol():
    if (n:= len(string)) < 3: ans.append(string + surprising)
    else:
        for i in range(n - 1):
            tmp = set()
            for j in range(n - i - 1):
                if (k := string[j] + string[j + i + 1]) in tmp:
                    ans.append(string + not_surprising); return
                else: tmp.add(k)
        ans.append(string + surprising)
input, ans = sys.stdin.readline, []
surprising, not_surprising = " is surprising.", " is NOT surprising."
while (string := input().strip()) != "*": sol()
print("\n".join(ans))