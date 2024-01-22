from sys import stdin
input = stdin.readline
N = int(input())
*A, = map(int, input().split())
B, C = map(int, input().split())
print(len(A)-sum(((B-a)//C for a in A if a>B)))