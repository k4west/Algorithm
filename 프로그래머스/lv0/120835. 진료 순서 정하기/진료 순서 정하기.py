def solution(emergency):
    return [sorted(emergency, reverse=True).index(n)+1 for n in emergency]