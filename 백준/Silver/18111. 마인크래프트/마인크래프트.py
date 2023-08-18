def sol():
    n, m, b = map(int, input().split())
    data = [0] * 257

    # 각 높이별로 등장하는 땅의 개수를 세는 작업
    for _ in range(n):
        for i in map(int, input().split()):
            data[i] += 1
    
    have = sum(i * data[i] for i in range(257))  # 현재 인벤토리에 가지고 있는 블록 수
    ans = (have * 2, 0)  # 초기 값으로 최대 시간과 땅의 높이를 설정
    need = 0
    t = data[0]  # 높이 0의 땅의 개수
    nm = n * m  # 집터의 총 땅의 개수

    # 높이를 1부터 256까지 순회하며 최소 시간과 땅의 높이를 갱신하는 작업
    for i in range(1, 257):
        need += t
        have -= nm - t
        t += data[i]
        
        if have + b - need < 0:
            # 인벤토리에 남은 블록 수가 필요한 블록 수보다 작아지면 종료
            break
        else:
            ans = min((have * 2 + need, -i), ans)  # 최소 시간과 최대 높이를 갱신
    
    print(ans[0], -ans[1])

sol()