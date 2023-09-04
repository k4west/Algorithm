def solution(id_pw, db):
    if id_pw in db:
        return "login"
    else:
        for i, p in db:
            if id_pw[0] == i and id_pw[1] != p:
                return "wrong pw"
        return "fail"