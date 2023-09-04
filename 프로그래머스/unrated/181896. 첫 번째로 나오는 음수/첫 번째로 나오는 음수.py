def solution(num_list):
    li = [i for i, s in enumerate(num_list) if s<0]
    return li[0] if li else -1

# def solution(num_list):
#     for i, n in enumerate(num_list):
#         if n < 0:
#             answer = i
#             return answer 
#     return -1

