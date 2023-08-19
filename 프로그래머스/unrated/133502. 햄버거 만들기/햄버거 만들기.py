def solution(ingredient):
    count = 0
    s = []
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1,2,3,1]:
            count +=1
            for _ in range(4):
                s.pop()
    return count

# def solution(ingredient):
#     s = "".join(map(str,ingredient))
#     n = len(ingredient)
#     while '1231' in s:
#         s = s.replace('1231','',1)
#     n -= len(s)
#     return n // 4