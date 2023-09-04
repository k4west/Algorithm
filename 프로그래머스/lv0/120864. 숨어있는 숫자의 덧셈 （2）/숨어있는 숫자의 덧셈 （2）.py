def solution(my_string):
    
    return sum(int(i) for i in ("".join([s if s.isdigit() else " " for s in my_string]).split()))