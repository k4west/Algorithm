def solution(order):
    truck, sub = 0, []; s = 1
    for i in order:
        f = True
        if s <= i:
            sub.extend([*range(s,i)])
            truck += 1
            f = False
            s = i+1
        elif sub and i == sub[-1]:
            sub.pop()
            truck+=1
            f = False
        if f: break
    return truck