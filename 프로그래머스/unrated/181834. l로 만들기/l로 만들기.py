def solution(myString):
    return "".join(["l" if s < 'l' else s for s in myString])