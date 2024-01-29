import sys


class Candy:
    def __init__(self):
        self.input = lambda: map(int, sys.stdin.readline().split())
        self.N, self.M, self.K = self.input()
        self.candies = [0] + list(self.input())
        self.friedns = [0] + [1 for _ in range(self.N)]
        self.roots = [i for i in range(self.N + 1)]

    def find_root(self, x):
        if x == (t := self.roots[x]):
            return x
        self.roots[x] = self.find_root(t)
        return self.roots[x]

    def union_root(self, x, y):
        if (a := self.find_root(x)) == (b := self.find_root(y)):
            return
        if a < b:
            self.roots[b] = a
            self.friedns[a] += self.friedns[b]
            self.candies[a] += self.candies[b]
        else:
            self.roots[a] = b
            self.friedns[b] += self.friedns[a]
            self.candies[b] += self.candies[a]
        return

    def sol(self):
        for _ in range(self.M):
            i, j = self.input()
            self.union_root(i, j)

        for i in range(1, self.N + 1):
            self.find_root(i)

        f_c = [
            (self.friedns[i], self.candies[i])
            for i in range(1, self.N + 1)
            if i == self.roots[i]
        ]
        f_c.sort(key=lambda x: (x[0], x[1]))

        dp = [0] * self.K
        for F, C in f_c:
            for i in range(self.K - 1, F - 1, -1):
                if dp[i] < (t := dp[i - F] + C):
                    dp[i] = t
        print(dp[self.K - 1])


if __name__ == "__main__":
    Candy().sol()