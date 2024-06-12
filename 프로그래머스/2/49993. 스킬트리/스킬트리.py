def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        s_ = skill
        i = 0
        for t in s:
            if t in s_:
                if t != s_[i]:
                    answer -= 1
                    break
                else:
                    i += 1
        answer +=1
    return answer