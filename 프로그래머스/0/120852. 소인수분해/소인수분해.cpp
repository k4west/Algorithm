#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    if (n%2 == 0) {
        answer.push_back(2);
        do n/=2;
        while (n%2==0);
    }
    for (int i=3; i*i<=n; i+=2) {
        if (n%i==0) {
            answer.push_back(i);
            do n/=i;
            while (n%i==0);
        }
    }
    if (n>1) answer.push_back(n);
    return answer;
}