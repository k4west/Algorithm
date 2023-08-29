import sys
while 1:
    li = sorted(map(lambda x:int(x)*int(x), sys.stdin.readline().rstrip().split()))
    if li[0] == 0:
        break
    if li[0]+li[1]==li[2]:
        print("right")
    else: print("wrong")