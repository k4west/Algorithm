import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    faculties = list(range(1, n + 1))
    opus_num = list(map(int, input().split()))
    idx = 0
    while n > 1:
        faculties.pop(idx := (idx + opus_num[idx] - 1) % n)
        opus_num.pop(idx)
        n -= 1
        idx %= n
    print(faculties[0])

if __name__ == "__main__":
    main()