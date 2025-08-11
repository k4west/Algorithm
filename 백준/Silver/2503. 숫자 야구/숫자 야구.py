cnt = 0
N = int(input())

tries = []
for _ in range(N):
    num, strike, ball = input().split()
    *nums, = map(int, num)
    strike, ball = map(int, (strike, ball))
    tries.append((nums, strike, ball))

for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            for k in range(1, 10):
                if i != k and j != k:

                    for nums, strike, ball in tries:
                        s = b = 0
                        
                        for n1, n2 in zip((i, j, k), nums):
                            if n1 == n2:
                                s += 1
                            elif n1 in nums:
                                b += 1

                        if s != strike or b != ball:
                            break
                    else:
                        cnt += 1

print(cnt)