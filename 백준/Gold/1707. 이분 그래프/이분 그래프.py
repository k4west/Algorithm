from collections import deque

def main():
    a = open(0)
    t = []
    for _ in range(int(next(a))):
        V, E = map(int, next(a).split())
        graph = [[] for _ in range(V+1)]
        color_li = [-1 for _ in range(V+1)]
        for _ in range(E):
            u, v = map(int, next(a).split())
            graph[u].append(v)
            graph[v].append(u)
        
        color = 0
        flag = False
        for i in range(1, V+1):
            if color_li[i] != -1:
                continue
            color_li[i] = color
            q = deque([i])
            while q:
                node = q.popleft()
                color = color_li[node] ^ 1
                for node1 in graph[node]:
                    if color_li[node1] == -1:
                        color_li[node1] = color
                        q.append(node1)
                    elif color_li[node1] != color:
                        flag = True
                        q = []
                        break
            if flag:
                break
        t.append('YNEOS'[flag::2])
    print('\n'.join(t))
main()