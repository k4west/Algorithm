import sys
def is_prime(x):
    for i in range(2, int(x**.5)+1):
        if x%i==0:
            return False
    return True

def main():
    T = int(sys.stdin.readline())
    li = [int(sys.stdin.readline()) for _ in range(T)]
    a = []
    for n in li:
        if n in (0, 1):
            a.append('2')
        else:
            while True:
                if is_prime(n):
                    a.append(str(n))
                    break
                n += 1
    print("\n".join(a))
    
if __name__=="__main__":
    main()