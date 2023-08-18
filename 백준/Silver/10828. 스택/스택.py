import sys
input = sys.stdin.readline

N = int(input())
op = [0] * N
for i in range(N):
    op[i] = list(map(str, input().split()))

class Stack:
    stack = []

    def push(self, n):
        self.n = n
        Stack.stack.append(self.n)

    def pop(self):
        if Stack.stack == []:
            print(-1)
        else :
            print(Stack.stack.pop())
    
    def size(self):
        print(len(Stack.stack))

    def empty(self):
        if len(Stack.stack) != 0:
            print(0)
        else:
            print(1)
    
    def top(self):
        if len(Stack.stack) == 0:
            print(-1)
        else:
            print(Stack.stack[-1])

for i in range(N):
    if len(op[i]) == 2:
        getattr(Stack(), op[i][0])(int(op[i][1]))
    else:
        getattr(Stack(), op[i][0])()