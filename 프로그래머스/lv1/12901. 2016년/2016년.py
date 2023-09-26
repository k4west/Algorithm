def solution(a, b):
    d = {0:"SUN",1:"MON",2:"TUE",3:"WED",4:"THU",5:"FRI",6:"SAT"}
    m = {1:0,2:3,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
    return d[(m[a]+b+4)%7]