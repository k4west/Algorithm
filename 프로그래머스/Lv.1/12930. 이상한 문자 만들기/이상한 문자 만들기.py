def solution(s):
    new_word = ''
    t = tt = 0
    for i, alpha in enumerate(s):
        if alpha == ' ':
            new_word += alpha
            t, tt = t+tt+1, 0
        elif (i-t)%2:
            new_word += alpha.lower()
            tt += 1
        else:
            new_word += alpha.upper()
            tt += 1
                
    return new_word