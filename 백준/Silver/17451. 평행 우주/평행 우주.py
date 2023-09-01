import sys
from math import lcm
N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
c_v = 0
# 마지막 행성 속도부터 시작해서 그 전 행성의 탈출 속도와 비교
for p_v in li[::-1]:
    # 이전 행성이 요구하는 속도가 더 빠를 때는 그 속도를 저장
    if c_v < p_v:
        c_v = p_v
    # 이전 행성이 요구하는 속도가 더 느리면서 
    elif c_v > p_v:
        # 약수가 아닐 때, 그 속도의 배수 중에 가장 가까운 큰 수를 속도로 저장
        if c_v % p_v:
            c_v = p_v*(c_v//p_v+1)

print(c_v)