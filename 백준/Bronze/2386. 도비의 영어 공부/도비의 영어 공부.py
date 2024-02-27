import sys

input = sys.stdin.readline
ans = []
while (string := input())[0] != "#":
    count = str(string[1:].lower().count((alpha := string[0])))
    ans.append(" ".join((alpha, count)))
print("\n".join(ans))