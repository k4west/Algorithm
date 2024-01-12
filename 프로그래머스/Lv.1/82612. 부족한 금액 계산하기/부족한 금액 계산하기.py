def solution(price, money, count):
    return max(price*(1+count)*(count)//2-money, 0)