def solution(arr, n):
    return [a + n if (i + len(arr) + 1) % 2 == 0 else a for i, a in enumerate(arr)]