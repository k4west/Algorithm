import sys
a, *arr, = map(int, sys.stdin.readline().split())
for b in arr:
    if a > b:
        print('Bad')
        break
    a = b
else:
    print('Good')