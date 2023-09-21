import sys
def f(d):
	li = []
	b = bin(d)[2:]
	for i, c in enumerate(b[::-1]):
		if c == '1':
			li.append(i)
	return li
def fr(li):
	n = 0
	for i in li:
		n += 2*4**i
	return n
def fc(li):
	n = 0
	for i in li:
		n += 4**i
	return n
if __name__ == "__main__":
    _, r, c = map(int, sys.stdin.readline().split())
    print(fr(f(r)) + fc(f(c)))