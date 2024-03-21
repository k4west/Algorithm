def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[-1])
    roots = [i for i in range(n)]
    
    def find_root(x):
        if x != (t:=roots[x]):
            roots[x] = roots[t]
        return roots[x]
    
    def union_root(x, y):
        if x < y:
            roots[y] = x
        else:
            roots[x] = y
        
        
    for a, b, cost in costs:
        if (x:=find_root(roots[a])) != (y:=find_root(roots[b])):
            union_root(x, y)
            for i in range(n):
                find_root(i)
            answer += cost
        
        if len(set(roots)) == 1:
            break
            
    return answer