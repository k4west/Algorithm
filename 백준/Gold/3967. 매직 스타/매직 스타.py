def check():
    for row in p:
        if sum(nums[idx] for idx in row) != 26:
            return False
    return True


def bt(d):
    global flag

    if flag or (all(nums[1:5]) and sum(nums[1:5]) != 26):
        return

    if d == 12:
        if check():
            flag = True
        return

    if nums[d]:
        bt(d+1)
        return

    for num in range(1, 13):
        if not v[num]:
            v[num] = 1
            nums[d] = num
            bt(d+1)
            v[num] = 0
            if flag:
                return
            nums[d] = 0


flag = False
p = (
    (0, 2, 5, 7),
    (1, 2, 3, 4),
    (0, 3, 6, 10),
    (7, 8, 9, 10),
    (1, 5, 8, 11),
    (4, 6, 9, 11)
)
stars = [list(input()) for _ in range(5)]
pos = []
nums = []
v = [0]*13
*candi, = range(1, 13)

for i in range(5):
    for j, k in enumerate(stars[i]):
        if k > '.':
            n = (ord(k)-64) % 56
            v[n] = 1
            nums.append(n)
            pos.append((i, j))

bt(0)
for (i, j), n in zip(pos, nums):
    stars[i][j] = chr(n+64)
print("\n".join("".join(row) for row in stars))
