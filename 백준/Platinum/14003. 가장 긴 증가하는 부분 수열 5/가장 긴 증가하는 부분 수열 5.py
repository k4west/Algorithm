import sys


def main():
    # 입력 받기
    input = sys.stdin.readline
    N = int(input())
    arr = tuple(map(int, input().split()))  # 수열

    # tmp: 증가하는 부분 수열을 저장하는 임시 리스트
    # order: 원소를 tmp에 저장할 때, 그 원소의 tmp내 index 값을 저장하는 리스트
    # ans: 가장 긴 증가하는 부분 수열을 저장하는 리스트
    tmp, order, ans = [], [], []

    # 수열의 원소를 하나씩 살펴보면서
    for i in range(N):
        a, s, e = arr[i], 0, len(tmp) - 1
        # 현재 원소가(=a) tmp 내에서
        while s <= e:
            m = (s + e) // 2
            # tmp내 m+1 번째 원소랑(=t) a랑 크기 비교
            # a가 작으면 더 작은 원소랑 비교하기 위해서 e=m-1
            if (t := tmp[m]) > a:
                e = m - 1
            # a가 크면 더 큰 원소랑 비교하기 위해서 s=m+1
            elif t < a:
                s = m + 1
            # a가 t와 같으면 s = m
            else:
                s = m
                break

        # >>> 0 <= s <= len(tmp)
        # s == len(tmp) -> a가 tmp내 모든 원소보다 큼
        # 아니면 증가하는 규칙에 맞게 tmp내 원소 수정
        if s == len(tmp):
            tmp.append(a)
        else:
            tmp[s] = a

        # order에 수열 내 a의 index와 같은 위치에 tmp내 순서를 저장
        # s는 index라서 s+1(순서)를 저장
        order.append(s + 1)

    print(n := len(tmp))  # 가장 긴 증가하는 부분 수열의 길이 출력

    # order내 저장된 순서 값을 역순으로 출력하면서
    # 순서(=n)에 맞는 원소를 ans에 저장하고 n -= 1로 그 전 순서로 바꿈
    for i in range(-1, -len(order) - 1, -1):
        if order[i] == n:
            ans.append(arr[i])
            n -= 1
    # 역순으로 저장된 ans를 역순으로 출력
    print(*ans[::-1])


if __name__ == "__main__":
    main()
