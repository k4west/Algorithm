def solution(name, yearning, photo):
    d = {k:v for k, v in zip(name, yearning)} # 딕셔러니 -> 이름: 점수
    return [sum(d.get(name, 0) for name in names) for names in photo] 
# dict.get(_key, default) : dict에 _key가 있으면 그 value를 반환하고, 없으면 default를 반환함