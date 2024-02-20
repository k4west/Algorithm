import sys

input = sys.stdin.readline
pangram = set(map(chr, range(97, 123)))
ans = []
for _ in range(int(input())):
    m = input().lower()
    if tmp := pangram - set(m):
        ans.append("missing " + "".join(sorted(tmp)))
    else:
        ans.append("pangram")
print("\n".join(ans))