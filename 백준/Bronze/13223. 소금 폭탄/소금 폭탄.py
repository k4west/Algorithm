now = sum(a*b for a, b in zip(map(int, input().split(':')), (3600, 60, 1)))
target = sum(a*b for a, b in zip(map(int, input().split(':')), (3600, 60, 1)))
time = (target - now) % 86400
print(':'.join(map(lambda x: str(x).zfill(2), (time//3600, (time:=time%3600)//60, time%60))) if time else '24:00:00')