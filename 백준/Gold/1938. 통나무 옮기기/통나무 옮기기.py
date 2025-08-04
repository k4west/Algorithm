def check(li):
    for x, y in li:
        if 0 <= x < N and 0 <= y < N and graph[x][y] != "1":
            continue
        else:
            return False
    return True


def rotate(li, s):
    x, y = li[1]
    if s == 'h':
        li = [(x-1, y), (x, y), (x+1, y)]
        s = 'v'
    else:
        li = [(x, y-1), (x, y), (x, y+1)]
        s = 'h'
    return li, s


d = ((-1, 0), (1, 0), (0, -1), (0, 1))     # 회전은 따로
N = int(input())
graph = []
visited = set()
log = []
goal = []

for i in range(N):
    row = input()
    graph.append(list(row))
    for j, k in enumerate(row):
        if k == 'B':
            log.append((i, j))
        if k == 'E':
            goal.append((i, j))

log.sort()
goal.sort()

# 'h': horizon, 'v': vertical
if log[0][0] == log[1][0]:
    log_state = 'h'
else:
    log_state = 'v'
# if goal[0][0] == goal[1][0]:
#     goal_state = 'h'
# else:
#     goal_state = 'v'

cnt = 1
q, nq = [(log, log_state)], []
visited.add((log[1], log_state))
flag = False
while q or nq:
    if not q:
        q, nq = nq, []
        cnt += 1

    cur, state = q.pop()
    for dr, dc in d:
        nxt = [(cur[i][0]+dr, cur[i][1]+dc) for i in range(3)]

        if nxt == goal:
            flag = True
            q = nq = []
            break

        elif check(nxt) and (nxt[1], state) not in visited:
            visited.add((nxt[1], state))
            nq.append((nxt, state))

    if state == 'h':
        box = [(i[0]+1, i[1]) for i in cur] + [(i[0]-1, i[1]) for i in cur]
    else:
        box = [(i[0], i[1]+1) for i in cur] + [(i[0], i[1]-1) for i in cur]

    if not flag and check(box):
        nxt, new_state = rotate(cur, state)
        if nxt == goal:
            flag = True
            break

        elif check(nxt) and (nxt[1], new_state) not in visited:
            visited.add((nxt[1], new_state))
            nq.append((nxt, new_state))

print(cnt if flag else 0)
