import sys
from datetime import datetime

input = lambda: datetime(*map(int, sys.stdin.readline().rstrip().split()))
ans = (input() - input()).days
print(f"D{ans}" if ans >= -365242 else "gg")