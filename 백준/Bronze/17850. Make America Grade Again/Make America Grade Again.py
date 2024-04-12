import sys

def main():
    input = sys.stdin.readline
    *per, n = map(int, input().split())
    d = {"Lab": [0, 0], "Hw": [0, 0], "Proj": [0, 0], "Exam": [0, 0]}
    for _ in range(n):
        assign, _, score = input().split()
        p, q = map(int, score.split("/"))
        d[assign][0] += p
        d[assign][1] += q
    print(int(sum(pp * p / q for pp, (p, q) in zip(per, d.values()))))

if __name__ == "__main__":
    sys.exit(main())