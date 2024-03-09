# 답은 피보나치 수열입니다.
# 아래 함수도 피보나치 수열을 구하는 함수로 볼 수도 있는데,
# 문제에 맞는 주석으로 설명을 적었습니다.

end_with_0, end_with_1 = 0, 1   # 초기 상태

# 0으로 끝나는 수는 이후에 0과 1을 이어서 적어도 된다.
# 1로 끝나는 수는 이후에 0만 이어 붙일 수 있다.

for _ in range(int(input())-1):
    # end_with_0, end_with_1 = end_with_0 + end_with_1, end_with_0
    # 아래 식은 위 주석처럼 한 줄로 처리할 수 있습니다.
     
    tmp = end_with_0
    end_with_0 += end_with_1
    end_with_1 = tmp

print(end_with_0+end_with_1)    # 합계 출력