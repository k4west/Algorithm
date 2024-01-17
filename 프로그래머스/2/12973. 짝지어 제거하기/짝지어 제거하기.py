def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
            continue
        stack.append(i)
    if stack:
        return 0
    return 1
        
# def solution(s):
#     n = len(s)    
#     if n%2:
#         return 0
    
#     while True:
#         t, ss = s, set(s)
#         for a in ss:
#             s = s.replace(a*2, '')
#         if not s:
#             return 1
#         if s == t:
#             return 0