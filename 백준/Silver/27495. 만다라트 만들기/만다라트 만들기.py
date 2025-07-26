mandarat = [input().split() for _ in range(9)]
mid_goals = [(mandarat[i+3][j+3], 3*i+1, 3*j+1) for i in range(3) for j in range(3) if i !=1 or j !=1]
mid_goals.sort()
sorted_mandarat = []
for idx, (mid_goal, i, j) in enumerate(mid_goals, 1):
    tmp = []
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if not di|dj:
                continue
            tmp.append(mandarat[i+di][j+dj])
    sub_idx = 0
    goals = []
    for goal in [mid_goal]+sorted(tmp):
        goal_str = f"#{idx}{-sub_idx if sub_idx else ''}. {goal}"
        goals.append(goal_str)
        sub_idx += 1
    sorted_mandarat.append('\n'.join(goals))
print('\n'.join(sorted_mandarat))