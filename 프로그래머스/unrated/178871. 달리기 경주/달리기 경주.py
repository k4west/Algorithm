from collections import deque

def solution(players, callings):
    p = {name:i for i, name in enumerate(players)}
    players = deque(players)
    for name in callings:
        i = p[name]
        p[name], p[players[i-1]] = i-1, i
        players[i], players[i-1] = players[i-1], players[i]
    return list(players)