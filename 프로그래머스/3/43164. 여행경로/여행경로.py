from collections import deque
def solution(tickets):
    n = len(tickets)
    ticket_dict = {}
    for dep, arr in tickets:
        if dep in ticket_dict:
            ticket_dict[dep].append(arr)
        else:
            ticket_dict[dep] = [arr]
    route = ['ICN']

    def bfs(dep):
        for arr in sorted(ticket_dict[dep]):
            route.append(arr)
            ticket_dict[dep].remove(arr)
            if arr in ticket_dict:
                bfs(arr)
            if len(route) == n+1:
                return route
            route.pop()
            ticket_dict[dep].append(arr)
    return bfs('ICN')
    