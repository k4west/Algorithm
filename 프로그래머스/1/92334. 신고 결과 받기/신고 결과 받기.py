def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict = {id: i for i, id in enumerate(id_list)}
    d = {}

    for s in report:
        a, b = s.split()
        if b in d:
            d[b].add(a)
        else: d[b] = {a}

    for l in d.values():
        if len(l) >= k:
            for a in l:
                answer[id_dict[a]] += 1
    return answer