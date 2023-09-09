import sys

def f(string):
    li = []
    for s in string:
        if s == "(" or s == "[":
            li.append(s)
        elif s == ")": 
            if li and li[-1] == "(":
                li.pop()
            else:
                li.append(s)
                break
        elif s == "]": 
            if li and li[-1] == "[":
                li.pop()
            else:
                li.append(s)
                break
    return "yes" if li==[] else "no"
    
while True:
    string = sys.stdin.readline().rstrip()
    if string == ".":
        break
    print(f(string))