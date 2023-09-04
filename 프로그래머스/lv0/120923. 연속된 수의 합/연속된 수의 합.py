def solution(num, total):
    return [i for i in range(total // num - (num-1) // 2,(total + (num+1) * num // 2) // num)]

