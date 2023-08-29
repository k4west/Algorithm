import sys
print(sum(map(lambda x:int(x)*int(x), sys.stdin.readline().strip().split()))%10)