import sys
import re
s = sys.stdin.readline().rstrip()
s = re.sub('1+', '1', re.sub('0+', '0', s))
print(len(s)//2)