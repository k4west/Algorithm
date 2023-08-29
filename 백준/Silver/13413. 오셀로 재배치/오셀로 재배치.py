import sys
T = int(sys.stdin.readline())
for _ in range(T):
    sys.stdin.readline()
    org = [1 if s=="W" else 0 for s in list(sys.stdin.readline().rstrip())]
    goal = [1 if s=="W" else 0 for s in list(sys.stdin.readline().rstrip())]
    diff = sum([1 if o!=g else 0 for o,g in zip(org, goal)])
    temp = abs(sum(org) - sum(goal))
    count = (diff+temp)//2 
    print(count)