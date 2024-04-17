N=int(input())
S=input()
C=S.count("C")
print(C//(N-C+1)+int(C%(N-C+1)>0))