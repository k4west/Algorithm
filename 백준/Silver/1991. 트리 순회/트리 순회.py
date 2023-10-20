from sys import stdin
input = stdin.readline
n = int(input())
graph = {}
for _ in range(n):
    p, l, r = input().rstrip().split()
    graph[p] = [l, r]

def f(s):
    tmp = s
    for a in graph[s]:
        if a == ".":
            continue
        tmp += f(a)
    return tmp

def m(s):
    tmp = s
    for i, a in enumerate(graph[s]):
        if a == ".":
            continue
        if i%2:
            tmp += m(a)
        else:
            tmp = m(a) + tmp
    return tmp

def b(s):
    tmp = ""
    for i, a in enumerate(graph[s]):
        if a == ".":
            continue
        if i%2:
            tmp += b(a)
        else:
            tmp = b(a)
    return tmp + s

print(f("A"), m("A"), b("A"), sep="\n")