def main():
    a = open(0)
    N = int(next(a))
    dist = [*map(int, next(a).split())]
    cost = [*map(int, next(a).split())]
    costs = 0
    cc = cost[0]
    for i in range(N-1):
        if cc > (t:=cost[i]):
            cc = t
        costs += dist[i]*cc
    print(costs)
main()