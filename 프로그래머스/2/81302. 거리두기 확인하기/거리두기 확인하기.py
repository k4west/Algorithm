d = ((0, 1), (1, 0), (0, -1), (-1, 0))

def check(i, j, graph, n):
    for dx, dy in d:
        if 0 <= (x:=i+dx) < 5 and 0 <= (y:=j+dy) < 5:
            if graph[x][y] == 'X':
                continue
            if graph[x][y] == 'P':
                return False
            if n and graph[x][y] == 'O':
                if not check(x, y, graph, False):
                    return False
    return True
    
def solution(places):
    answer = []
    for graph in places:
        graph = [list(row) for row in graph]
        flag = True
        for i in range(25):
            if graph[(x:=i//5)][(y:=i%5)] == 'P':
                graph[x][y] = 'X'
                if not (flag:=check(x, y, graph, True)):
                    answer.append(0)
                    break
        if flag:
            answer.append(1)
            
    return answer