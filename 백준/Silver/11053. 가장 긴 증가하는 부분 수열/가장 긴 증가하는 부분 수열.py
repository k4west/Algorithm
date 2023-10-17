from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
li = [1]*N

for i in range(N):
    a = A[i]
    for j in range(i+1, N):
        if A[j] > a:
            li[j] = max(li[j], li[i]+1)
print(max(li))