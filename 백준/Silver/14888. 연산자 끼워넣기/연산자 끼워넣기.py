def bt(depth, op_str):
    global min_val, max_val

    if depth == N-1:
        val = A[0]
        for op, num in zip(op_str, A[1:]):
            if op == '+':
                val += num
            if op == '-':
                val -= num
            if op == '*':
                val *= num
            if op == '/':
                if val*num < 0:
                    val //= -num
                    val *= -1
                else:
                    val //= num
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val
        return

    for i in range(N-1):
        if not visited[i]:
            visited[i] = 1
            bt(depth+1, op_str+ops[i])
            visited[i] = 0


N = int(input())
*A, = map(int, input().split())
visited = [0]*(N-1)
ops = ''.join(op*c for op, c in zip('+-*/', map(int, input().split())))

INF = float("inf")
max_val = -INF
min_val = INF

bt(0, "")
print(max_val)
print(min_val)
