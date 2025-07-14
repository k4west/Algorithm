points = sorted([[*map(int, input().split())] for _ in range(int(input()))])
print('\n'.join(' '.join(map(str, i)) for i in points))