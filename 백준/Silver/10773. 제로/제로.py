import sys
input = sys.stdin.readline

K = int(input())

temp = []
for _ in range(K):
    k = int(input())
    if k == 0:
        temp.pop()
    else:
        temp.append(k)

print(sum(temp))