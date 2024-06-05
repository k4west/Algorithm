def is_prime(n):
    if n == 2:return True
    elif n==1 or n%2==0:return False
    for i in range(3, int(n**.5)+1, 2):
        if n%i==0:return False
    return True
def solution(n, k):
    answer = 0
    s=[]
    while n:s.append(n%k);n//=k
    s=''.join(map(str, s[::-1])).split('0')
    d={}
    for i in s:
        if i:d[i]=d.get(i,0)+1
    for i, j in d.items():
        if is_prime(int(i)):answer+=j
    return answer