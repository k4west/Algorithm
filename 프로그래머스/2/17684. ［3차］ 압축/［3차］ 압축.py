d={chr(i+64):i for i in range(1, 27)}
def solution(msg):
    answer=[];i=26;t=''
    for s in msg:
        if t+s in d:t+=s
        else:answer.append(d[t]);i+=1;d[t+s]=i;t=s
    answer.append(d[t])
    return answer