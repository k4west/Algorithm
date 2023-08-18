import sys
input = sys.stdin.readline

input()
A = set(input().split())
input()
answer = ['1' if b in A else '0' for b in input().split()]
print(*answer, sep="\n")