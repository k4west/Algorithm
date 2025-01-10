S = int(input())
for i in range(1, 92683):
    if (s:=i*(i+1)//2) >= S:
        print(i-(s!=S))
        break