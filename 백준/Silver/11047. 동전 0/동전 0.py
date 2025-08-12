# 동전은 총 N종류이고, 가치의 합을 K로 만들기
# 필요한 동전 개수의 최솟값

# 각각의 동전을 매우 많이 가지고 있다

N, K = map(int, input().split())        # (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
A = [int(input()) for _ in range(N)]    # 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

cnt = 0
for i in range(N-1, -1, -1):        # 큰 금액의 동전부터
    coin = A[i]
    if K >= coin:                   # 합산할 수 있는 금액이면
        q, K = K//coin, K % coin    # 반복문 대신 나누기를 활용
        cnt += q
print(cnt)
