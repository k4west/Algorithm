import sys
# 반지름, 행성의 중심과 시작점/도착점 사이의 거리 비교
# root를 씌우기 보다 모두 제곱한 상태로 비교했습니다.
def f(x1, y1, x2, y2):
    cx, cy, r = map(int, sys.stdin.readline().split())  # 행성의 정보: 중심, 반지름 입력 
    r *= r
    d1, d2 = (cx-x1)**2 + (cy-y1)**2, (cx-x2)**2 + (cy-y2)**2
    
    # 시작점/도착점 중 한 점은 원의 내부에 다른 한 점은 원의 내부에 있으면 집입/이탈이 필요
    if d1 < r < d2 or d2 < r < d1:  # 집입/이탈이 필요한 경우 > 횟수 추가  
        return 1
    return 0    # 아니면 횟수 변동 x

def main():
    T = int(sys.stdin.readline())   # 테스트 횟수
    for _ in range(T):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split()) # 출발점과 도착점 입력 받기
        n = int(sys.stdin.readline())   # 행성의 개수 입력 받기

        s = 0
        for _ in range(n):      # 각 행성에 대해 집입/이탈이 필요한지 확인
            s += f(x1, y1, x2, y2)
        print(s)          # 최소 집입/이탈 횟수 출력

if __name__=="__main__":
    main()