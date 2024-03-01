import sys
input = sys.stdin.readline
ans = []
while (s := input())[0] != "0": ans.append(("No", "Yes")[eval(s.replace(" ", ">"))])
print("\n".join(ans))