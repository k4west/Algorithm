import sys
input = sys.stdin.readline
a = ((16,8),(8,6),(8,4),(8,2),(16,8))
n = int(input())
m = int(input())
n -= 1
print(n + a[n][0]*(m//2) + a[n][1]*(m%2))