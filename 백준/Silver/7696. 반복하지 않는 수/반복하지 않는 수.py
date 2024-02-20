from itertools import permutations, chain, islice
from math import factorial

ans = []
while True:
    n = int(input())
    if n == 0: break
    ans.append("".join(map(str, next(islice(chain(*map(lambda x: islice(permutations(range(10), x), factorial(9) // factorial(9 - x + 1), None),range(1, 11))), n - 1, None)))))
print("\n".join(ans))