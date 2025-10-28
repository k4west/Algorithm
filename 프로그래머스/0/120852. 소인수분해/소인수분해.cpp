#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    if (n%2 == 0) {
        answer.push_back(2);
    }
    vector<bool> isnotprime(n+1);
    for (int i=3; i<=n; i+=2) {
        if (not isnotprime[i] and (n%i == 0)) {
            answer.push_back(i);
            for (int j=i*i; j<=n; j+=i) {
                isnotprime[j] = true;
            }
        }
    }
    return answer;
}