def solution(myStr):
    myStr = myStr.replace("b", "a")
    myStr = myStr.replace("c", "a")
    myStr = [s for s in list(myStr.split("a")) if s]
    return myStr if myStr else ["EMPTY"]