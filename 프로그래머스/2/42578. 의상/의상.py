# def solution(clothes):
#     d = {}
#     for cloth, types in clothes:
#         if types in d:
#             d[types].append(cloth)
#         else:
#             d[types] = [cloth]
#     s = 1
#     for i in d.values():
#         s *= len(i) + 1
#     return s - 1

# def solution(clothes):
#     d = {}
#     for _, types in clothes:
#         d[types] = d.get(types, 0) + 1
#     s = 1
#     for i in d.values():
#         s *= i + 1
#     return s - 1

def solution(clothes):
    d = {}
    for types in [a for a in zip(*clothes)][1]:
        d[types] = d.get(types, 0) + 1
    s = 1
    for i in d.values():
        s *= i + 1
    return s - 1