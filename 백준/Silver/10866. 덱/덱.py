import sys
input = sys.stdin.readline

N = int(input())
l = [0] * N
for i in range(N):
    l[i] = list(map(str,input().split()))

class Deque:
    deque = []

    def push_front(self, n):
        self.n = n
        Deque.deque.insert(0, self.n)

    def push_back(self, n):
        self.n = n
        Deque.deque.append(self.n)

    def pop_front(self):
        if Deque.deque == []:
            print(-1)
        else :
            print(Deque.deque.pop(0))

    def pop_back(self):
        if Deque.deque == []:
            print(-1)
        else :
            print(Deque.deque.pop())
    
    def size(self):
        print(len(Deque.deque))

    def empty(self):
        if len(Deque.deque) != 0:
            print(0)
        else:
            print(1)

    def front(self):
        if len(Deque.deque) == 0:
            print(-1)
        else:
            print(Deque.deque[0])

    def back(self):
        if len(Deque.deque) == 0:
            print(-1)
        else:
            print(Deque.deque[-1])

for i in range(N):
    if len(l[i]) == 2:
        getattr(Deque(), l[i][0])(int(l[i][1]))
    else:
        getattr(Deque(), l[i][0])()