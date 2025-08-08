N = int(input())
*A, = map(int, input().split())
ans, stack = [], []

# 지금 높이 보다 높은 탑 중에서 가장 왼쪽에 있는 높은 탑의 순서를 알고 싶음
# 왼쪽 탑부터 높이를 확인
for i, a in enumerate(A, 1):
    # 높이가 같은 경우는 없기 때문에 등호는 신경 안써도 됩니다.
    while stack and stack[-1][0] < a:   # 지금 탑보다 작은 탑의 기록은 필요 없어서 pop
        stack.pop()
    if not stack:                       # 지금 탑보다 높은 탑이 왼쪽에 없으면 0
        ans.append(0)
    else:
        ans.append(stack[-1][1])        # 있으면 순서를 저장
    stack.append((a, i))                # 비교할 높이와 저장할 순서를 `stack`에 push
print(' '.join(map(str, ans)))