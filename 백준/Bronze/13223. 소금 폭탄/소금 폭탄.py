def time2sec(h, m, s):
    return h*3600 + m*60 + s
now = time2sec(*map(int, input().split(':')))
time = time2sec(*map(int, input().split(':')))
time -= now
if time <= 0:
    time += 86400
h, m, s = time//3600, (time:=time%3600)//60, time%60
print(f'{h:02d}:{m:02d}:{s:02d}')