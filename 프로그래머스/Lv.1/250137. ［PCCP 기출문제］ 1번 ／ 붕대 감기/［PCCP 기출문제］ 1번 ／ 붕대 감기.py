def solution(bandage, health, attacks):
    M = health
    t, x, y = bandage
    time = 1
    gauge = 0
    for a_time, damge in attacks:
        while time != a_time:
            gauge += 1
            if gauge == t:
                health = min(M, health+x+y)
                gauge = 0
            else:
                health = min(M, health+x)
            time += 1
        health -= damge
        if health <= 0:
            return -1
        gauge = 0
        time += 1
    return health