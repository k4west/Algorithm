def solution(rank, attendance):
    return sum([rank.index(b)*(100**(2-i)) for i, b in enumerate(sorted([r for r, a in zip(rank, attendance) if a])[:3])])