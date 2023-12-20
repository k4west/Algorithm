def solution(survey, choices):
    types = {c:0 for c in "RTCFJMAN"}
    score = {1:(3,0), 2:(2,0), 3:(1,0), 4:(0,0), 5:(0,1), 6:(0,2), 7:(0,3)}
    for t, choice in zip(survey, choices):
        t1, t2 = t[0], t[1]
        s1, s2 = score[choice][0], score[choice][1]
        if s1: types[t1] += s1
        if s2: types[t2] += s2
    return "".join([t1 if types[t1] >= types[t2] else t2 for t1, t2 in zip("RCJA","TFMN")])