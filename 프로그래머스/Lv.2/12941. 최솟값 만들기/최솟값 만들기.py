def solution(A,B):
    s = 0
    for a, b, in zip(sorted(A), sorted(B, reverse=True)):
        s += a*b
    return s