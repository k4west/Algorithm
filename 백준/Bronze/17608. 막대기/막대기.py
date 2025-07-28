N, *sticks = map(int, open(0))
cnt = max_h = 0
for _ in range(N):
    h = sticks.pop() # 바라보는 곳 기준으로 가까운 막대기부터 먼 막대기 순서대로 확인    
    if h > max_h:    # 더 높은 막대기가 있으면
        max_h = h    # 최대 높이 수정
        cnt += 1     # 개수 증가
print(cnt)