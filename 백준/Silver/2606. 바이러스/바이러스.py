import sys
input = sys.stdin.readline

A = [0] * int(input())
A[0] = 1

M = int(input())
ab = []
for i in range(M):
    ab.append(list(map(int,input().split())))
    
for _ in A:
    for i in range(M):
        if A[ab[i][0] - 1] != A[ab[i][1] - 1]:
            A[ab[i][0] - 1] = 1
            A[ab[i][1] - 1] = 1

print(sum(A)-1)