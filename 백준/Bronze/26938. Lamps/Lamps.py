h, P = map(int, input().split())
d = 1
while 60*h*d*P/100000+(d*h//1000+int(d*h%1000>0))*5 <= 11*h*d*P/100000+(d*h//8000+int(d*h%8000>0))*60:
    d += 1
print(d)