def solution(friends, gifts):
    x = lambda: {friend: 0 for friend in friends}
    d = {friend: x() for friend in friends}
    p = x()
    for gift in gifts:
        A, B = gift.split()
        d[A][B] += 1
        p[A] += 1
        p[B] -= 1
    ans = x()
    n = len(friends)
    for i in range(n):
        for j in range(i+1, n):
            A, B = friends[i], friends[j]
            if (da:=d[A][B]) > (db:=d[B][A]):
                ans[A] += 1
            elif da < db:
                ans[B] += 1
            elif (pa:=p[A]) > (pb:=p[B]):
                ans[A] += 1
            elif pa < pb:
                ans[B] += 1
    
    return max(ans.values())