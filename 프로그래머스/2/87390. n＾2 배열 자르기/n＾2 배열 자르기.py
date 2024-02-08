def solution(n, left, right):
    return [max(divmod(idx, n))+1 for idx in range(left, right+1)]
