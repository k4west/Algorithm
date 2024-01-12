def solution(absolutes, signs):
    return sum([n if s else -n for n, s in zip(absolutes, signs)])