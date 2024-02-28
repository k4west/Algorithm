import sys

input = lambda: map(int, sys.stdin.readline().split())
input()
trees = list(set(input()))
apples = set(input())

trees.sort()
m_dist = float("inf")

for num in apples:
    left, right = 0, len(trees) - 1
    while left <= right:
        mid = (left + right) // 2
        dist = abs(trees[mid] - num)
        m_dist = min(m_dist, dist)
        if trees[mid] < num:
            left = mid + 1
        elif trees[mid] > num:
            right = mid - 1
        else:
            break
    if m_dist == 0:
        break
print(m_dist)