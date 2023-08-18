import sys
input = sys.stdin.readline

N = int(input())
l = [0] * N
for i in range(N):
    l[i] = list(map(str,input().split()))

class Queue:
    queue = []

    def push(self, n):
        self.n = n
        Queue.queue.append(self.n)

    def pop(self):
        if Queue.queue == []:
            print(-1)
        else :
            print(Queue.queue.pop(0))
    
    def size(self):
        print(len(Queue.queue))

    def empty(self):
        if len(Queue.queue) != 0:
            print(0)
        else:
            print(1)

    def front(self):
        if len(Queue.queue) == 0:
            print(-1)
        else:
            print(Queue.queue[0])

    def back(self):
        if len(Queue.queue) == 0:
            print(-1)
        else:
            print(Queue.queue[-1])

for i in range(N):
    if len(l[i]) == 2:
        getattr(Queue(), l[i][0])(int(l[i][1]))
    else:
        getattr(Queue(), l[i][0])()