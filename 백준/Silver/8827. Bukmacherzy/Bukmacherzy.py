for _ in range(int(input())):
    X, Y = map(float, input().split())
    print(["NIE", "TAK"][(X - 1) * (Y - 1) > 1])