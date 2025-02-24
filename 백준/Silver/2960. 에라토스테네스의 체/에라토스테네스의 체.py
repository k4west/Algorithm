def main():
    N, K = map(int, input().split())
    nums = [False, False] + [True for _ in range(N-1)]
    for i in range(2, N+1):
        if nums[i]:
            K -= 1
            if K==0: return i
            for j in range(i*i, N+1, i):
                if nums[j]:
                    K -=1
                    nums[j] = False
                    if K == 0: return j
print(main())