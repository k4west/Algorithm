A,B,C = int(input()), int(input()), int(input())
for i in range(10):
    print(str(A*B*C).count('%d'%(i)))