import sys


def main():
    inf = 32768
    low = -inf
    high = inf
    low_flag = high_flag = False
    ans = set()

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
                # a <= x <= b
                ans |= set(range(a, b + 1))

    if low_flag:
        # -32768 <= x < low
        ans |= set(range(-inf, low + 1))
        # high <= x <= 32767
    if high_flag:
        ans |= set(range(high, inf))

    # x에 해당하는 값 존재
    if ans:
        # 모두 존재
        if len(ans) == 2 * inf:
            print("true")
        # 일부 존재
        else:
            tmp = []
            ans = sorted(ans)
            # 초기 값 a: 시작, b: 마지막
            a = b = ans[0]
            for c in ans[1:]:
                # 다음 값이 연속되는 정수이면 b 값 업데이트
                if b == c - 1:
                    b = c
                # 아니면 x >= a && x <= b 기록후 c값으로 a, b 업데이트
                else:
                    tmp.append(f"x >= {a} && x <= {b}")
                    a = b = c
            # 마지막 범위 업데이트
            tmp.append(f"x >= {a} && x <= {b}")

            # 불필요하다면 x >= -32768, x <= 32767 제거
            tmp[0] = tmp[0].replace(f"x >= {-inf} && ", "")
            tmp[-1] = tmp[-1].replace(f" && x <= {inf-1}", "")
            print(" ||\n".join(tmp))
    # 범위에 해당하는 값이 하나도 없음
    else:
        print("false")


main()