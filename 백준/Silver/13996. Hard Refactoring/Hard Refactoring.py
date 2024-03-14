import sys


def preprocess():
    low = -inf
    high = inf
    low_flag = high_flag = False
    nums = set()
    tmp = []

    for line in sys.stdin:
        # 입력 받은 값에서 || 지우고, %%를 기준으로 분리
        line = line.strip().replace("||", "").split("&&")
        n = len(line)

        # 비교식 1개
        if n == 1:
            if "<" in line[0]:
                low = max(low, int(line[0].split("= ")[1]))
                low_flag = True
            else:
                high = min(high, int(line[0].split("= ")[1]))
                high_flag = True
        # 비교식 2개
        else:
            a, b = int(line[0].split("= ")[1]), int(line[1].split("= ")[1])
            if a <= b:
                tmp.append((a, b))

    if tmp:
        tmp.sort()
        a0, b0 = tmp[0]
        for a1, b1 in tmp[1:]:
            if a1 <= b0 + 1:
                if b0 < b1:
                    b0 = b1
            else:
                nums |= set(range(a0, b0 + 1))
                a0, b0 = a1, b1
        nums |= set(range(a0, b0 + 1))

    if low_flag:
        # -32768 <= x < low
        nums |= set(range(-inf, low + 1))
        # high <= x <= 32767
    if high_flag:
        nums |= set(range(high, inf))

    return nums


def sol():
    # x에 해당하는 값 존재
    if nums := preprocess():
        # 모두 존재 -> true
        if len(nums) == 2 * inf:
            print("true")
        # 일부 존재 -> 범위 출력
        else:
            ans = []
            nums = sorted(nums)
            # 초기 값 a: 시작, b: 마지막
            a = b = nums[0]
            for c in nums[1:]:
                # 다음 값이 연속되는 정수이면 b 값 업데이트
                if b == c - 1:
                    b = c
                # 아니면 x >= a && x <= b 기록후 c값으로 a, b 업데이트
                else:
                    ans.append(f"x >= {a} && x <= {b}")
                    a = b = c
            # 마지막 범위 업데이트
            ans.append(f"x >= {a} && x <= {b}")

            # x >= -32768, x <= 32767 제거
            ans[0] = ans[0].replace(f"x >= {-inf} && ", "")
            ans[-1] = ans[-1].replace(f" && x <= {inf-1}", "")
            print(" ||\n".join(ans))
    # 범위에 해당하는 값이 하나도 없음 -> false
    else:
        print("false")


if __name__ == "__main__":
    inf = 32768
    sol()