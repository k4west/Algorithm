def sum4(A, B, C, D):
    """
    A와 B에 있는 원소로 만들 수 있는 합의 모든 경우를 생성
    C와 D도 똑같이 합해서 AB에 상응 하는 값이 있는지 확인
    """
    dct = {}
    count = 0
    for a in A:
        for b in B:
            dct[ab] = dct.get((ab := a+b), 0) + 1
    for c in C:
        for d in D:
            count += dct.get(-c-d, 0)
    return count


if __name__ == "__main__":
    Arr = [[], [], [], []]
    for row in open(0).read().split('\n'):
        if ' ' not in row:
            continue
        for i, num in enumerate(map(int, row.split(' '))):
            Arr[i].append(num)
    print(sum4(*Arr))
