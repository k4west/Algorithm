import sys
input = sys.stdin.readline

answer = {}
for _ in range(int(input())):
    name, log = input().split()
    if log == "enter": answer[name] = 1
    else: del answer[name]
print("\n".join(sorted(answer.keys(), reverse=True)))