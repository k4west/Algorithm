import sys
input = sys.stdin.readline
a2c = {}
for _ in range(26):
    a, c = input().rstrip().split()
    a2c[a] = c
d = {}
for _ in range(int(input())):
    word = input().rstrip()
    m = "".join(a2c[w] for w in word)
    d[m] = word
ans = []
while n := int(input()):
    tmp = []
    flag = True
    for _ in range(n):
        if not flag:
            input()
            continue
        if (m := input().rstrip()) in d:
            tmp.append(d[m])
        else:
            tmp = [m, "not in dictionary."]
            flag = False
    ans.append(" ".join(tmp))
print("\n".join(ans))