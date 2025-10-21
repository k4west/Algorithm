#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<bool> isPrime(n+1, true);
    isPrime[0] = false;
    isPrime[1] = false;
    for (int i=2; i*i<=n; i++) {
        if (isPrime[i]) {
            for (int j=i+i; j<=n; j+=i) {
                if (isPrime[j]) {
                    isPrime[j] = false;
                    answer++;
                }
            }
        }
    }
    
    return answer;
}