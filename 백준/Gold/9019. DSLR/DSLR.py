import sys
from collections import deque
input = sys.stdin.readline

def main():
    dslr = DSLR()   # 클래스 호출
    for _ in range(int(input())):
        s, e = map(int, input().split())
        dslr.input_data(s, e)
    dslr.p()    # 정답 출력

class DSLR:
    def __init__(self):
        self.li = []    # 출력할 명령어 나열을 저장할 리스트

    # 큐를 사용해서 주어진 정수 A, B를
    # A는 DSLR 연산을, B는 DSLR 연산을 반대로 취해서
    # 중간 지점에서 만날 때까지 탐색하는 함수
    def searching(self):
        while True:
            xs, ys = self.sq.popleft(), self.eq.popleft()
            self.xt = []
            self.yt = []

            # DSLR 연산을 수행한 결과를 큐에 저장
            for x in xs:
                x0 = (x<<1)%10000
                if self.fx(x, x0, "D"): return
                x1 = (x-1)%10000
                if self.fx(x, x1, "S"): return
                x2 = (x*10)%10000 + x//1000
                if self.fx(x, x2, "L"): return
                x3 = x%10*1000 + x//10
                if self.fx(x, x3, "R"): return
            self.sq.append(self.xt)

            # DSLR 연산을 반대로 수행한 결과를 큐에 저장
            for y in ys:
                if not y%2:
                    y0 = y>>1
                    if self.fy(y, y0, "D"): return
                    y0 += 5000
                    if self.fy(y, y0, "D"): return
                y1 = (y+1)%10000
                if self.fy(y, y1, "S"): return
                y2 = y%10*1000 + y//10
                if self.fy(y, y2, "L"): return
                y3 = (y*10)%10000 + y//1000
                if self.fy(y, y3, "R"): return
            self.eq.append(self.yt)

    # DSLR 연산 후 처음 방문한 정수는 연산을 기록해서 방문을 표시하고 
    # 반대쪽이 도달한 정수와 겹치면 두 연산 기록을 합쳐서 self.li에 기록
    def fx(self, x: int, nx: int, op: str):
        if nx not in self.sd:
            self.sd[nx] = self.sd[x] + op
            if nx in self.ed:
                self.li.append(self.sd[nx] + self.ed[nx])
                return True
            self.xt.append(nx)

    # DSLR 연산을 반대로 수행 후 나머지는 self.fx와 같음
    def fy(self, y: int, ny: int, op: str):
        if ny not in self.ed:
            self.ed[ny] = op + self.ed[y]
            if ny in self.sd:
                self.li.append(self.sd[ny] + self.ed[ny])
                return True
            self.yt.append(ny)

    # 입력 받은 두 정수로 탐색할 큐와 방문 기록할 딕셔너리를 각각 생성 후 탐색 함수 실행
    def input_data(self, s: int, e: int):
        self.sd = {s: ""}
        self.ed = {e: ""}
        self.sq = deque([[s]])
        self.eq = deque([[e]])
        self.searching()
    
    def p(self):
        print("\n".join(self.li))


if __name__ == "__main__":
    main()