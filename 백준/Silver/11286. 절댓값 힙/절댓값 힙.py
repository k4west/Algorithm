import heapq
import sys
def f():
    N = int(sys.stdin.readline())
    li, t = [], []  
    for _ in range(N):
        n = int(sys.stdin.readline())
        if n == 0:
            if li:
                t.append(str(heapq.heappop(li)[1]))
            else:
                t.append("0")
        else:
            heapq.heappush(li, (abs(n), n))   
    print("\n".join(t))
if __name__ == "__main__":
    f()