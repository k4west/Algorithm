import sys
def f(N):
    li = [tuple(sys.stdin.readline().split()) for _ in range(N)]
    li.sort(key=lambda x:x[1], reverse=True)
    li.sort(key=lambda x:x[0])
    li = [" ".join(m) for m in li]
    return li
li = f(int(sys.stdin.readline()))
print("\n".join(li))