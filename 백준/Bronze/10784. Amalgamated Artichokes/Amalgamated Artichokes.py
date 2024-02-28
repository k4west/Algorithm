import sys
from math import sin, cos

p, a, b, c, d, n = map(int, sys.stdin.readline().split())

m_price = 0
m_decline = 0
for k in range(1, n + 1):
    price = p * (sin(a * k + b) + cos(c * k + d) + 2)
    if m_price < price:
        m_price = price
    elif m_decline < (decline := m_price - price):
        m_decline = decline
print(m_decline)