import sys

def f(string):
    li = []
    d = {")":"(", "]":"["}
    for s in string:
        if s == "(" or s == "[":
            li.append(s)
        elif s in d: 
            if li and li[-1] == d[s]:
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