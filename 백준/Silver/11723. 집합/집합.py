import sys

class set_op:
    def __init__(self):
        self.S = set()
    
    def add(self, x):
        self.S.add(x)
    
    def remove(self, x):
        self.S.discard(x)
        
    def check(self, x):
        print(int(x in self.S))
        
    def toggle(self, x):
        if x in self.S:
            self.S.discard(x)
        else:
            self.S.add(x)
    
    def all(self):
        self.S = set(range(1, 21))
    
    def empty(self):
        self.S.clear()
        
T = int(sys.stdin.readline())
S = set_op()
for _ in range(T):
    op, *val = sys.stdin.readline().rstrip().split()
    if val:
        x = int(val[0])
        if op == "add":
            S.add(x)
        elif op == "remove":
            S.remove(x)
        elif op == "check":
            S.check(x)
        elif op == "toggle":
            S.toggle(x)
    else:
        if op == "all":
            S.all()
        elif op == "empty":
            S.empty()