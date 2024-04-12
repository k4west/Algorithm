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
    s = 0
    for pp, (p, q) in zip(per, d.values()):
        s += pp * p / q
    print(int(s))

if __name__ == "__main__":
    sys.exit(main())