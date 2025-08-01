F, S, G, U, D = map(int, input().split())

if S == G or (S > G and D) or (S < G and U):
    INF = float("inf")
    floors = [INF]*(F+1)

    q = [S] if S != G else []
    buttons = (U, -D)
    floors[S] = 0

    while q:
        cf = q.pop(0)
        for move in buttons:
            nf = cf + move
            if nf == G:
                floors[nf] = floors[cf] + 1
                q = []
                break
            if 0 < nf <= F and floors[nf] == INF:
                floors[nf] = floors[cf] + 1
                q.append(nf)

    if floors[G] != INF:
        print(floors[G])
    else:
        print("use the stairs")
else:
    print("use the stairs")