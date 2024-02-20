def sol(length, num, flag, digits):
    global idx
    if idx > M: return
    if not length:
        nums[idx] = num
        idx += 1
        return
    for digit in digits:
        if flag and digit == 0: continue
        tmp = [i for i in digits]
        tmp.remove(digit)
        sol(length - 1, num + digit * (10 ** (length - 1)), False, tmp)


def main():
    ans = []
    for length in range(1, 9):
        sol(length, 0, True, list(range(10)))

    while True:  # 계속 입력을 받다가 입력이 0인 경우 종료
        if (i := int(input())) == 0: break
        ans.append(nums[i])
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    import sys

    input = lambda: int(sys.stdin.readline())  # 입력 값을 숫자로 변환
    M, idx = 1_000_000, 1
    nums = [0] * (M + 1)  # 정답을 모아 둘 리스트
    main()