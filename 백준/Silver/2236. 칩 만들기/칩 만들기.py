N, K = map(int, input().split())
arr = sorted(zip(map(int, input().split()), range(N)))
connected_chips = ["0"] * N
powers = ["0"] * K
for i, (_, j) in enumerate(arr[::-1][:K]):
    powers[i] = j + 1
    connected_chips[j] = j + 1
print("\n".join(map(str, powers + connected_chips)))