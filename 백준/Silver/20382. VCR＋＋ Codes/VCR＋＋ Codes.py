import sys
mon2num = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
ans = []
for a in sys.stdin.readlines():
    ch, date, time = a.split(",")
    ch = int(ch[8:])
    month, days, year = date.split()
    month = mon2num[month]
    start, length, _ = time.split("m")
    length, days, year, hour, minute = map(int, [length, days, year] + start[:-1].split(':'))
    hour %= 12
    if start[-1] == 'p':
        hour += 12
    start = hour * 2 + minute//30
    year = bin(year-1994)[2:].zfill(7)
    ch = bin(ch)[2:].zfill(6)
    month = bin(month)[2:].zfill(4)
    days = bin(days)[2:].zfill(5)
    start = bin(start)[2:].zfill(6)
    length = bin(length//30)[2:].zfill(4)
    code = year + ch + month + days + start + length
    ans.append(int(code, 2))
print("\n".join(map(str, ans)))