def solution(routes):
    answer = 1
    routes.sort()
    past_in, past_out = routes[0]
    for now_in, now_out in routes[1:]:
        if past_out < now_in:
            past_in, past_out = now_in, now_out
            answer += 1
        elif past_out > now_out:
            past_out = now_out
    return answer