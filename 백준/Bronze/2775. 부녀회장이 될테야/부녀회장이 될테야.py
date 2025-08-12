# 초기값
# 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다
dp = [[i for i in range(15)]] + [[0]*15 for _ in range(14)]     # 1 ≤ k, n ≤ 14

# 점화식
# a층의 b호: 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합
for a in range(1, 15):
    for b in range(1, 15):
        dp[a][b] = dp[a-1][b] + dp[a][b-1]

# 답 구하기
ans = []
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    ans.append(dp[k][n])    # k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지

print("\n".join(map(str, ans)))
