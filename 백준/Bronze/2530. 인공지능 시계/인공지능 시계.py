h, m, s = map(int, input().split())
t = int(input())
t += h*3600 + m*60 + s
h = (t//3600)%24
m = (t%3600)//60
s = t%60
print(f'{h} {m} {s}')