import sys
def hhmm2min(t: str) -> int:
    t = list(map(int, t.split(":")))
    return t[0] % 12 * 60 + t[1]
def compare(t1, t2, t3):
    if (diff := (t2 - t1)%720) == (t3 - t2)%720: return diff
    return 0
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    tmp = []
    t1, t2, t3 = map(hhmm2min, input().rstrip().split())
    for a, b, c in ((t1, t2, t3), (t1, t3, t2), (t2, t1, t3), (t2, t3, t1), (t3, t1, t2), (t3, t2, t1),):
        if diff := compare(a, b, c):
            if diff == 240: ans.append("Look at the sun")
            elif diff < 480: ans.append(f"The correct time is {b // 60 or 12}:{str(b % 60).zfill(2)}")
            else: continue
            break
print("\n".join(ans))