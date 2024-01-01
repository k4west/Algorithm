import sys

def main():
    n, c = sys.stdin.readline().rstrip(), 0
    
    # 한자리수가 될 때까지 자리수 더하기
    while len(n) != 1:
        n = str(sum(int(i)*n.count(i) for i in '123456789'))
        c += 1
    
    print(c)    # 횟수 출력
    if not int(n)%3:
        print('YES')
    else: print('NO')

if __name__ == '__main__':
    main()