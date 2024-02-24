from sys import stdin

def main():
    input = stdin.readline
    ans = []
    ing = "SYJKGW"
    for _ in range(int(input())):
        # t: 현재 땅에 있는 병사 수. li: 각각 병사의 군대 번호가 담긴 리스트
        t, *li = input().rstrip().split()
        li = tuple(li)

        # 절반을 초과해야 지배하므로 다른 군대의 병사 수를 합친 것보다 많아야 함
        major, count = 0, 0
        for n in li:
            if count == 0:
                major, count = n, 1
            elif major == n:
                count += 1
            else:
                count -= 1
        # 절반 초과시 지배 / 아니면 전쟁 중
        if li.count(major) > int(t) // 2:
            ans.append(major)
        else:
            ans.append(ing)
    print("\n".join(ans))

if __name__ == "__main__":
    main()