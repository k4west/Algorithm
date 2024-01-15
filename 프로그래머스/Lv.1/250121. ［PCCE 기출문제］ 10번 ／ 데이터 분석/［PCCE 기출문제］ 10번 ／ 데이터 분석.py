def solution(data, ext, val_ext, sort_by):
    d = {'code': 0,	'date': 1, 'maximum': 2, 'remain':3}
    i = d[ext]
    j = d[sort_by]
    return sorted([a for a in data if a[i] < val_ext], key=lambda x: x[j])