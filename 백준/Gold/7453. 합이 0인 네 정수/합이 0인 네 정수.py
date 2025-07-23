def sum2(A, B, C, D):
    AB = [a+b for a in A for b in B]
    CD = [-c-d for c in C for d in D]
    AB.sort()
    CD.sort()
    return AB, CD

def sum4(AB, CD, n):
    count = i = j = 0
    N = n*n
    while i < N and j < N:
        if (ab := AB[i]) == (cd := CD[j]):
            ti = tj = 1
            while i < N-1 and AB[i+1] == ab:
                i += 1
                ti += 1
            while j < N-1 and CD[j+1] == cd:
                j += 1
                tj += 1
            count += ti*tj
            i += 1
        elif ab < cd:
            i += 1
        else:
            j += 1

    return count


def main():
    n, *arr = open(0).read().split('\n')
    n = int(n)
    Arr = [[], [], [], []]  # A, B, C, D

    for row in arr:
        if not row.strip('\n'):
            break
        for i, num in enumerate(map(int, row.split(' '))):
            Arr[i].append(num)

    AB, CD = sum2(*Arr)
    print(sum4(AB, CD, n))


if __name__ == "__main__":
    main()
