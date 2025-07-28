N = int(input())
*tang, = map(int, input().split())
fruits = [0] * 10   # 과일 종류별 개수를 저장하는 리스트
max_cnt = s = num_f = 0

for e, f in enumerate(tang):
    # 처음 보는 과일 -> num_f 증가
    if not fruits[f]:
        num_f += 1
    fruits[f] += 1

    # 과일 종류 개수 > 2 -> 과일 빼기
    while num_f > 2:
        fruits[(old_f := tang[s])] -= 1

        # 과일 종류 개수, 없앨 과일 인덱스 반영
        if not fruits[old_f]:
            num_f -= 1
        s += 1

    # 과일의 개수가 가장 많은 탕후루의 과일 개수
    if max_cnt < e-s+1:
        max_cnt = e-s+1

print(max_cnt)