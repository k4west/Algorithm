import sys
input=sys.stdin.readline
n=int(input())
grid=[input().rstrip() for _ in range(n)]
ans=1

def more_than_3(line):
    count,prev=0,"W"
    for s in line:
        if s==prev: 
            if (count:=count+1)==3:return True
        else:count,prev=1,s
    return False

for maps in (grid,zip(*grid)):
    for line in maps:
        if line.count("W")!=n//2:ans=0;break
        if more_than_3(line):ans=0;break
    if not ans: break
print(ans)