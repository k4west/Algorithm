from itertools import permutations


def sol(index):
    score = idx = 0
    for res in results:
        out = plates = 0
        while out < 3:
            r = res[index[idx]]
            if r == 0:
                out += 1
            else:
                plates <<= r
                plates |= 1 << r-1
                score += (plates >> 3).bit_count()
                plates &= 7
            idx = (idx+1) % 9
    return score


ans = 0
nums = [1, 2, 3, 4, 5, 6, 7, 8]
N = int(input())
results = [[*map(int, input().split())] for _ in range(N)]

for li in map(list, permutations(nums, 8)):
    li = li[:3] + [0] + li[3:]
    tmp = sol(li)
    if ans < tmp:
        ans = tmp
print(ans)