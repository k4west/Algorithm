def solution(distance, rocks, n):
    answer = 0
    s, e = 1, distance
    rocks.sort()
    rocks.append(e)
    while s <= e:
        prev = cnt = 0
        tmp, m = distance, (s+e)//2
        for rock in rocks:
            if (d:=rock - prev) < m:
                cnt += 1
                if cnt > n: break
            else: prev = rock
        if cnt > n: e = m-1
        else:
            answer = m
            s = m+1
    return answer