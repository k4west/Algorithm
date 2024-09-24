t = input()
def cc(a):
    if 64<ord(a)<91:return chr((ord(a)-65+i)%26+65)
    return a
for i in range(26):
    b = ''.join(map(cc,t))
    if 'CHIPMUNKS' in b and 'LIVE' in b:
        print(b)
        break