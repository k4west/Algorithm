import sys
n = int(sys.stdin.readline())
st_id = [""]*n
for i in range(n):
    st_id[i] = sys.stdin.readline().rstrip()
while 1:
    st_id = [s[1:] for s in st_id]
    if len(set(st_id)) != n:
        print(len(st_id[0])+1)
        break