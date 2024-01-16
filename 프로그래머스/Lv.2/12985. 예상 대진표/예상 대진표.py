def solution(n,a,b):
    # return ((a-1)^(b-1)).bit_length()
    i = 1
    a -= 1
    b -= 1
    while True:
        a, b = a >> 1, b >> 1
        if a == b:
            return i
        i += 1