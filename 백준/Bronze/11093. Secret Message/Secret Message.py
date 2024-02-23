import sys
input = sys.stdin.readline
for _ in range(int(input())):
    k = int((len(message:= input().rstrip()) - 1) ** 0.5) + 1
    print("".join(message[i::k][::-1] for i in range(k)))