import sys
input = sys.stdin.readline
pangram = set(map(chr, range(97, 123)))
for _ in range(int(input())):
    if tmp:=pangram-set(input().lower()): print("missing " + "".join(sorted(tmp)))
    else: print("pangram")