import sys
from collections import deque
input = sys.stdin.readline

class DSLR:
    def __init__(self):
        self.li = []

    def searching(self):
        while True:
            xs, ys = self.sq.popleft(), self.eq.popleft()
            self.xt = []
            self.yt = []
            flag = False

            for x in xs:
                x0 = (x<<1)%10000
                if self.fx(x, x0, "D"):
                    flag = True
                    break
                x1 = (x-1)%10000
                if self.fx(x, x1, "S"):
                    flag = True
                    break
                x2 = (x*10)%10000 + x//1000
                if self.fx(x, x2, "L"):
                    flag = True
                    break
                x3 = x%10*1000 + x//10
                if self.fx(x, x3, "R"):
                    flag = True
                    break
            if flag: break
            self.sq.append(self.xt)

            for y in ys:
                if not y%2:
                    y0 = y//2
                    if self.fy(y, y0, "D"):
                        flag = True
                        break
                    y0 += 5000
                    if self.fy(y, y0, "D"):
                        flag = True
                        break
                y1 = (y+1)%10000
                if self.fy(y, y1, "S"):
                    flag = True
                    break
                y2 = y%10*1000 + y//10
                if self.fy(y, y2, "L"):
                    flag = True
                    break
                y3 = (y*10)%10000 + y//1000
                if self.fy(y, y3, "R"):
                    flag = True
                    break
            if flag: break
            self.eq.append(self.yt)

    def fx(self, x: int, nx: int, op: str):
        if nx not in self.sd:
            self.sd[nx] = self.sd[x] + op
            if nx in self.ed:
                self.li.append(self.sd[nx] + self.ed[nx])
                return True
            self.xt.append(nx)

    def fy(self, y: int, ny: int, op: str):
        if ny not in self.ed:
            self.ed[ny] = op + self.ed[y]
            if ny in self.sd:
                self.li.append(self.sd[ny] + self.ed[ny])
                return True
            self.yt.append(ny)

    def input_data(self, s, e):
        self.sd = {s: ""}
        self.ed = {e: ""}
        self.sq = deque([[s]])
        self.eq = deque([[e]])
        self.searching()
    
    def p(self):
        print("\n".join(self.li))


if __name__ == "__main__":
    dslr = DSLR()
    for _ in range(int(input())):
        s, e = map(int, input().split())
        dslr.input_data(s, e)
    dslr.p()
