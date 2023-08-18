year = int(input())
if (year % 4 == 0 and year % 25 != 0) or year % 16 == 0:
    print(1)
else: 
    print(0)