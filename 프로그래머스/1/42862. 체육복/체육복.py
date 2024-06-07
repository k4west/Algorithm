def solution(n, lost, reserve):
    lo = set(lost) - set(reserve)
    re = set(reserve) - set(lost)
    
    for r in re:
        if r-1 in lo:
            lo.remove(r-1)
        elif r+1 in lo:
            lo.remove(r+1)

    return n-len(lo)