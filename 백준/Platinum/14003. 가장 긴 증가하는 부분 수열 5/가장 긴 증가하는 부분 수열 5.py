import sys
from bisect import bisect_left


def main():
    # 입력 받기
    input = sys.stdin.readline
    N = int(input())
    arr = tuple(map(int, input().split()))  # 수열

    # tmp: 증가하는 부분 수열을 저장하는 리스트
    # order: 원소를 tmp에 저장할 때, 그 원소의 tmp내 순서 값을 저장하는 리스트
    tmp, order = [arr[0]], [1]

    # 수열의 원소를 하나씩 살펴보면서
    for a in arr[1:]:
        if a > tmp[-1]:
            tmp.append(a)
            order.append(len(tmp))
        else:
            idx = bisect_left(tmp, a)
            tmp[idx] = a
            order.append(idx + 1)
    print(n := len(tmp))  # 가장 긴 증가하는 부분 수열의 길이 출력
    
    # order내 저장된 순서 값을 역순으로 출력하면서
    # 순서(=n)에 맞는 원소를 tmp에 저장하고 n -= 1로 그 전 순서로 바꿈
    for i in range(-1, -len(order) - 1, -1):
        if order[i] == n:
            tmp[n - 1] = str(arr[i])
            n -= 1
    print(" ".join(tmp))


if __name__ == "__main__":
    main()