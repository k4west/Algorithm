import sys
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    message = input().rstrip()
    L = len(message)
    while True:
        if L==(k:=L**.5)**2: k=int(k); break
        L += 1
    message = message.ljust(L, "*")
    ans.append("".join(("".join(message[j*k+i] for j in range(k-1, -1, -1))for i in range(k))).replace("*", ""))
print("\n".join(ans))