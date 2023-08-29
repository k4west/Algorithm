import sys
T = int(sys.stdin.readline())
for _ in range(T):
    sys.stdin.readline()
    org = sys.stdin.readline().rstrip()
    goal = sys.stdin.readline().rstrip()
    diff = sum([1 if o!=g else 0 for o,g in zip(org, goal)])
    temp = abs(org.count("W") - goal.count("W"))
    count = (diff+temp)//2 
    print(count)