import sys
print(eval("-".join(map(lambda x: str(sum(map(int, x.split('+')))), sys.stdin.readline().rstrip().split('-')))))