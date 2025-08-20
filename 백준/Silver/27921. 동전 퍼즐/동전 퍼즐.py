# 두 모형을 겹쳐서 일치하는 최대 동전의 개수를 구해보자
total = overlap = 0
H1, W1 = map(int, input().split())
before = [[0]*20 for _ in range(20)]  # 현재 동전의 배치
for r in range(H1):
    for c, s in enumerate(input()):
        if s == 'O':
            before[r][c] = 1
            total += 1

H2, W2 = map(int, input().split())
after = [[0]*20 for _ in range(20)]   # 만들어야 하는 동전의 배치
for r in range(H2):
    for c, s in enumerate(input()):
        if s == 'O':
            after[r][c] = 1


def check_overlap(di, dj):    # before는 그냥 두고 after를 옮겨 가며 시도하자.
    global overlap

    tmp = 0
    for i in range(H1):
        for j in range(W1):
            tmp += before[i][j] & after[i+di][j+dj]
    if overlap < tmp:
        overlap = tmp


for dr in range(max(H1, H2)):
    for dc in range(max(W1, W2)):        # (0, 0) 4번 중복 -> 3번 제외 -> 굳이;;
        check_overlap(-dr, dc)
        check_overlap(dr, dc)
        check_overlap(-dr, -dc)
        check_overlap(dr, -dc)

print(total - overlap)  # 옮겨야 하는 동전의 개수는 최소 몇 개인지