import sys
sys.stdin.readline()
s = set(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
li = ['1' if i in s else '0' for i in map(int, sys.stdin.readline().split())]
print(*li)