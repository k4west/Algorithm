import sys
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    message = input().rstrip()
    k = int((len(message) - 1) ** 0.5) + 1
    ans.append("".join(message[i::k][::-1] for i in range(k)))
print("\n".join(ans))