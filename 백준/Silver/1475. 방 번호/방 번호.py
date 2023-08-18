import sys
from math import ceil

input = sys.stdin.readline()
N = list(i for i in input.strip())
di = {}
for j in range(10):
    j = str(j)
    if j == '9':
        di['6'] = ceil((di['6'] + N.count('9')) / 2)
    else: di[j] = N.count(j)
print(max(di.values()))