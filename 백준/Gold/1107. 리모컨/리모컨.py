import sys
def main():
    input = sys.stdin.readline
    N = input().rstrip()
    M = input().rstrip()

    count = abs(int(N)-100)
    if M == '10': return count
    
    btn = {i for i in range(10)} - set(map(int, input().split()))
    
    q = [""]
    while q:
        p = q.pop(0)
        for n in btn:
            tmp = p + str(n)
            count = min(count, abs(int(N) - int(tmp)) + len(tmp))
            if len(tmp) < 6:
                q.append(tmp)
    return count

if __name__=="__main__":
    print(main())