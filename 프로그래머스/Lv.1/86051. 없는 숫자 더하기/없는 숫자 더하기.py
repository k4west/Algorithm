def solution(numbers):
    ans = 45 
    for n in numbers:
        ans -= n
    return ans