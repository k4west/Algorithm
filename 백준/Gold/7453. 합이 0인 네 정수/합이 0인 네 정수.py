n, *arr = open(0).read().split('\n')
n = int(n)
Arr = [[], [], [], []]  # A, B, C, D

for row in arr:
    if not row.strip('\n'):
        break
    for i, num in enumerate(map(int, row.split(' '))):
        Arr[i].append(num)

AB = [a + b for a in Arr[0] for b in Arr[1]]
CD = [c + d for c in Arr[2] for d in Arr[3]]
AB.sort()
CD.sort()

count = i = 0
N = j = n * n - 1
while i <= N and j >= 0:
    if (ab := AB[i]) == -(cd := CD[j]):
        ti = tj = 1
        while i < N and AB[i + 1] == ab:
            i += 1
            ti += 1
        while j > 0 and CD[j - 1] == cd:
            j -= 1
            tj += 1
        count += ti * tj
        i += 1
    elif ab < -cd:
        i += 1
    else:
        j -= 1

print(count)
