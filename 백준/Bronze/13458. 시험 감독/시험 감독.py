N, *A, B, C = map(int, open(0).read().split())
print(len(A)-sum((B-a)//C for a in A if a>B))