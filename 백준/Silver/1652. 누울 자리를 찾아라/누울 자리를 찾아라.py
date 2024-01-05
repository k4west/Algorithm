f = lambda rows: sum(sum(1 for i in "".join(row).rstrip().split('X') if len(i) > 1) for row in rows)
N, *rows = open(0)
print(f(rows), f(zip(*rows)))