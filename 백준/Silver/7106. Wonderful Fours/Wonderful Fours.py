from itertools import combinations, permutations
def main():
    ss = sorted({int(''.join(i)) for i in permutations(sorted(input().split()), 5) if i[0]!='0'}) #96 or 120
    print(sum(1 for i in combinations(range(len(ss)), 4) if ss[i[0]]+ss[i[1]]+ss[i[2]] == ss[i[3]]))
main()