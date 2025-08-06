def bt(depth, val):
    global min_val, max_val

    if depth == N-1:
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val
        return

    for i in range(N-1):
        if not visited[i]:
            visited[i] = 1
            op = ops[i]
            if op == '+':
                n_val = val + A[depth+1]
            if op == '-':
                n_val = val - A[depth+1]
            if op == '*':
                n_val = val * A[depth+1]
            if op == '/':
                if val*A[depth+1] < 0:
                    n_val = -(val // -A[depth+1])
                else:
                    n_val = val // A[depth+1]
            bt(depth+1, n_val)
            visited[i] = 0


N = int(input())
*A, = map(int, input().split())
visited = [0]*(N-1)
ops = ''.join(op*c for op, c in zip('+-*/', map(int, input().split())))

INF = float("inf")
max_val = -INF
min_val = INF

bt(0, A[0])
print(max_val)
print(min_val)
