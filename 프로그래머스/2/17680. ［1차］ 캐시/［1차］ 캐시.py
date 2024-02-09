from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    ans = n = 0
    tmp = deque([])
    for city in cities:
        if (city:=city.upper()) in tmp:
            ans += 1
            del tmp[tmp.index(city)]
        else:
            ans += 5
            if len(tmp) == cacheSize:
                tmp.popleft()
        tmp.append(city)
        
    return ans