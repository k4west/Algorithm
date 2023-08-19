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