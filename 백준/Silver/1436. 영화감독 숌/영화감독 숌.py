def main():
    s = 666
    for _ in range(int(input())-1):
        s += 1
        while "666" not in str(s): s += 1
    print(s)
main()