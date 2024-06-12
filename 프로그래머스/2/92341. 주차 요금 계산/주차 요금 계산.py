def solution(fees, records):
    t0, p0, t1, p1 = fees
    answer = []
    d = {}
    last = '23:59'
    for record in records:
        i = 1
        time, car, desc = record.split()
        if car not in d:
            d[car] = [[],[]]
        if desc == 'IN':
            i-=1
        d[car][i].append(time)
    for _, v in sorted([(k, v) for k, v in d.items()], key=lambda x: x[0]):
        if len(v[0])!=len(v[1]): v[1].append(last)
        t = 0
        for in_t, out_t in zip(sorted(v[0]),sorted(v[1])):
            hi, mi = map(int,in_t.split(':'))
            ho, mo = map(int,out_t.split(':'))
            if mi > mo:
                t += 60 - (mi - mo)
                ho -= 1
            else: t += mo - mi
            t += (ho - hi) * 60
        if (t:=t-t0)<=0: answer.append(p0)
        else: answer.append(p0+(t//t1+int(t%t1>0))*p1)
    return answer