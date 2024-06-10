for A,B,T in map(lambda x: map(int,x.split()),open(0).readlines()[1:]):
    while B:A,B=B,A%B
    print(T//A)