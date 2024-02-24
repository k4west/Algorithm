import sys
input = sys.stdin.readline
print("\n".join(['yes' if 6 < len(input()) < 11 else 'no' for _ in range(int(input()))]))