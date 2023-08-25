# def move(s,e,a,n,li):
#     if n == 1:
#         li.append([s,e])
#         return
#     move(s,a,e,n-1,li)
#     li.append([s,e])
#     move(a,e,s,n-1,li)

# def solution(n):
#     li = []
#     move(1,3,2,n,li)
#     return li

def move(s,e,a,n):
    if n == 0:
        return []
    return move(s,a,e,n-1) + [[s,e]] + move(a,e,s,n-1)
def solution(n):
    return move(1,3,2,n)